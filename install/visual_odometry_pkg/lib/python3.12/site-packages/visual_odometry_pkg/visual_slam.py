#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry

from cv_bridge import CvBridge


class VisualSLAM(Node):

    def __init__(self):

        super().__init__('visual_slam')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(
            nfeatures=1500
        )

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        self.prev_gray = None
        self.prev_kp = None
        self.prev_desc = None

        self.position = np.zeros((3, 1))
        self.rotation = np.eye(3)

        self.place_database = []

        self.frame_count = 0

        self.K = np.array([
            [525.0, 0.0, 320.0],
            [0.0, 525.0, 240.0],
            [0.0, 0.0, 1.0]
        ])

        self.odom_pub = self.create_publisher(
            Odometry,
            '/visual_slam_odom',
            10
        )

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

        if (
            self.prev_desc is not None and
            len(desc) > 20
        ):

            matches = self.matcher.match(
                self.prev_desc,
                desc
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

                    self.position += self.rotation @ t
                    self.rotation = R @ self.rotation

                    odom = Odometry()

                    odom.header.stamp = (
                        self.get_clock().now().to_msg()
                    )

                    odom.header.frame_id = "map"

                    odom.pose.pose.position.x = float(
                        self.position[0]
                    )

                    odom.pose.pose.position.y = float(
                        self.position[1]
                    )

                    odom.pose.pose.position.z = float(
                        self.position[2]
                    )

                    self.odom_pub.publish(odom)

        best_score = 0
        best_place = -1

        for idx, stored_desc in enumerate(
            self.place_database
        ):

            matches = self.matcher.match(
                stored_desc,
                desc
            )

            score = len([
                m for m in matches
                if m.distance < 50
            ])

            if score > best_score:

                best_score = score
                best_place = idx

        if best_score > 100:

            self.get_logger().info(
                f'Loop Closure: '
                f'Place={best_place} '
                f'Score={best_score}'
            )

        if self.frame_count % 30 == 0:

            self.place_database.append(desc)

        self.prev_gray = gray
        self.prev_kp = kp
        self.prev_desc = desc

        self.get_logger().info(
            f'Visual SLAM Pose: '
            f'({self.position[0][0]:.2f}, '
            f'{self.position[1][0]:.2f}, '
            f'{self.position[2][0]:.2f})'
        )


def main(args=None):

    rclpy.init(args=args)

    node = VisualSLAM()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
