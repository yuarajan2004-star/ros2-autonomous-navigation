#!/usr/bin/env python3

import cv2
import numpy as np

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class RANSACFeatureMatching(Node):

    def __init__(self):

        super().__init__('ransac_feature_matching')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(500)

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

            if len(matches) > 8:

                src_pts = np.float32(
                    [
                        self.prev_kp[m.queryIdx].pt
                        for m in matches
                    ]
                ).reshape(-1, 1, 2)

                dst_pts = np.float32(
                    [
                        kp[m.trainIdx].pt
                        for m in matches
                    ]
                ).reshape(-1, 1, 2)

                H, mask = cv2.findHomography(
                    src_pts,
                    dst_pts,
                    cv2.RANSAC,
                    5.0
                )

                if mask is not None:

                    inlier_matches = [
                        matches[i]
                        for i in range(len(matches))
                        if mask[i]
                    ]

                    output = cv2.drawMatches(
                        cv2.cvtColor(
                            self.prev_gray,
                            cv2.COLOR_GRAY2BGR
                        ),
                        self.prev_kp,
                        frame,
                        kp,
                        inlier_matches,
                        None
                    )

                    cv2.imshow(
                        "RANSAC Matches",
                        output
                    )

                    cv2.waitKey(1)

                    self.get_logger().info(
                        f'Total={len(matches)} '
                        f'Inliers={len(inlier_matches)}'
                    )

        self.prev_gray = gray
        self.prev_kp = kp
        self.prev_desc = desc


def main(args=None):

    rclpy.init(args=args)

    node = RANSACFeatureMatching()

    rclpy.spin(node)

    node.destroy_node()

    cv2.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
