#!/usr/bin/env python3

import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class FeatureMatcher(Node):

    def __init__(self):

        super().__init__('feature_matcher')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(
            nfeatures=500
        )

        self.matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        self.prev_frame = None
        self.prev_keypoints = None
        self.prev_descriptors = None

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

        keypoints, descriptors = self.orb.detectAndCompute(
            gray,
            None
        )

        if (
            self.prev_descriptors is not None and
            descriptors is not None
        ):

            matches = self.matcher.match(
                self.prev_descriptors,
                descriptors
            )

            matches = sorted(
                matches,
                key=lambda x: x.distance
            )

            output = cv2.drawMatches(
                self.prev_frame,
                self.prev_keypoints,
                frame,
                keypoints,
                matches[:50],
                None,
                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
            )

            cv2.imshow(
                "Feature Matches",
                output
            )

            cv2.waitKey(1)

            self.get_logger().info(
                f"Matches: {len(matches)}"
            )

        self.prev_frame = frame.copy()
        self.prev_keypoints = keypoints
        self.prev_descriptors = descriptors


def main(args=None):

    rclpy.init(args=args)

    node = FeatureMatcher()

    rclpy.spin(node)

    node.destroy_node()

    cv2.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
