#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class StereoVision(Node):

    def __init__(self):

        super().__init__('stereo_vision')

        self.bridge = CvBridge()

        self.left_image = None
        self.right_image = None

        self.stereo = cv2.StereoBM_create(
            numDisparities=64,
            blockSize=15
        )

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

        self.compute_disparity()

    def right_callback(self, msg):

        self.right_image = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='mono8'
        )

        self.compute_disparity()

    def compute_disparity(self):

        if (
            self.left_image is None or
            self.right_image is None
        ):
            return

        disparity = self.stereo.compute(
            self.left_image,
            self.right_image
        )

        disparity = cv2.normalize(
            disparity,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        disparity = np.uint8(disparity)

        cv2.imshow(
            "Stereo Disparity",
            disparity
        )

        cv2.waitKey(1)

        self.get_logger().info(
            "Stereo disparity computed"
        )


def main(args=None):

    rclpy.init(args=args)

    node = StereoVision()

    rclpy.spin(node)

    node.destroy_node()

    cv2.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
