#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class StereoCameraPublisher(Node):

    def __init__(self):

        super().__init__('stereo_camera_publisher')

        self.bridge = CvBridge()

        self.cap = cv2.VideoCapture(0)

        self.left_pub = self.create_publisher(
            Image,
            '/camera_left/image_raw',
            10
        )

        self.right_pub = self.create_publisher(
            Image,
            '/camera_right/image_raw',
            10
        )

        self.timer = self.create_timer(
            1.0 / 30.0,
            self.timer_callback
        )

    def timer_callback(self):

        ret, frame = self.cap.read()

        if not ret:
            return

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        h, w = gray.shape

        shift = 30

        left_img = gray.copy()

        right_img = np.zeros_like(gray)

        right_img[:, :-shift] = gray[:, shift:]

        left_msg = self.bridge.cv2_to_imgmsg(
            left_img,
            encoding='mono8'
        )

        right_msg = self.bridge.cv2_to_imgmsg(
            right_img,
            encoding='mono8'
        )

        self.left_pub.publish(left_msg)
        self.right_pub.publish(right_msg)


def main(args=None):

    rclpy.init(args=args)

    node = StereoCameraPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
