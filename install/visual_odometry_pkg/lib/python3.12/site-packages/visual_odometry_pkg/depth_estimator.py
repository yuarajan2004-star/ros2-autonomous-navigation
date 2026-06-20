#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class DepthEstimator(Node):

    def __init__(self):

        super().__init__('depth_estimator')

        self.bridge = CvBridge()

        self.left_image = None
        self.right_image = None

        self.stereo = cv2.StereoBM_create(
            numDisparities=64,
            blockSize=15
        )

        self.baseline = 0.10
        self.focal_length = 525.0

        self.left_sub = self.create_subscription(
            Image,
            '/camera_left/image_raw',
            self.left_callback,
            10
        )

        self.right_sub = self.create_subscription(
            Image,
            '/camera_right/image_raw',
            self.right_callback,
            10
        )

    def left_callback(self, msg):

        self.left_image = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='mono8'
        )

        self.compute_depth()

    def right_callback(self, msg):

        self.right_image = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='mono8'
        )

        self.compute_depth()

    def compute_depth(self):

        if self.left_image is None:
            return

        if self.right_image is None:
            return

        disparity = self.stereo.compute(
            self.left_image,
            self.right_image
        ).astype(np.float32)

        disparity[disparity <= 0] = 0.1

        depth = (
            self.focal_length *
            self.baseline
        ) / disparity

        center_depth = depth[
            depth.shape[0] // 2,
            depth.shape[1] // 2
        ]

        self.get_logger().info(
            f'Center Depth: {center_depth:.2f} m'
        )


def main(args=None):

    rclpy.init(args=args)

    node = DepthEstimator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
