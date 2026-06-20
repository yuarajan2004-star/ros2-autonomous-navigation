#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class EssentialMatrixEstimator(Node):

    def __init__(self):

        super().__init__('essential_matrix_estimator')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(1000)

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        self.prev_gray = None
        self.prev_kp = None
        self.prev_desc = None

        self.sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        # Approximate camera matrix
        self.K = np.array([
            [525.0, 0.0, 320.0],
            [0.0, 525.0, 240.0],
            [0.0, 0.0, 1.0]
        ])

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

        if (
            self.prev_desc is not None and
            desc is not None
        ):

            matches = self.matcher.match(
                self.prev_desc,
                desc
            )

            matches = sorted(
                matches,
                key=lambda x: x.distance
            )

            if len(matches) > 20:

                pts1 = np.float32([
                    self.prev_kp[m.queryIdx].pt
                    for m in matches
                ])

                pts2 = np.float32([
                    kp[m.trainIdx].pt
                    for m in matches
                ])

                E, mask = cv2.findEssentialMat(
                    pts1,
                    pts2,
                    self.K,
                    cv2.RANSAC,
                    0.999,
                    1.0
                )

                if E is not None:

                    _, R, t, _ = cv2.recoverPose(
                        E,
                        pts1,
                        pts2,
                        self.K
                    )

                    self.get_logger().info(
                        f'Translation: '
                        f'[{t[0][0]:.3f}, '
                        f'{t[1][0]:.3f}, '
                        f'{t[2][0]:.3f}]'
                    )

                    self.get_logger().info(
                        f'Rotation Matrix:\n{R}'
                    )

        self.prev_gray = gray
        self.prev_kp = kp
        self.prev_desc = desc


def main(args=None):

    rclpy.init(args=args)

    node = EssentialMatrixEstimator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
