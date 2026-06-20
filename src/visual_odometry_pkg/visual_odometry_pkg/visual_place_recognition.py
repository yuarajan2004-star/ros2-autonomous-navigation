#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class VisualPlaceRecognition(Node):

    def __init__(self):

        super().__init__('visual_place_recognition')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(
            nfeatures=1000
        )

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        self.database = []

        self.frame_count = 0

        self.sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

    def image_callback(self, msg):

        frame = self.bridge.imgmsg_to_cv2(
            msg,
            desired_encoding='bgr8'
        )

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        kp, desc = self.orb.detectAndCompute(
            gray,
            None
        )

        if desc is None:
            return

        self.frame_count += 1

        best_score = 0
        best_place = -1

        for idx, stored_desc in enumerate(self.database):

            matches = self.matcher.match(
                stored_desc,
                desc
            )

            good_matches = [
                m for m in matches
                if m.distance < 50
            ]

            score = len(good_matches)

            if score > best_score:

                best_score = score
                best_place = idx

        if best_score > 80:

            self.get_logger().info(
                f'Place Recognized: '
                f'Place {best_place} '
                f'Score={best_score}'
            )

        if self.frame_count % 30 == 0:

            self.database.append(desc)

            self.get_logger().info(
                f'New Place Stored: '
                f'{len(self.database)-1}'
            )


def main(args=None):

    rclpy.init(args=args)

    node = VisualPlaceRecognition()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
