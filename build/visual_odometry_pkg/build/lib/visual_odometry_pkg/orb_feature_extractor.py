#!/usr/bin/env python3

import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image

from cv_bridge import CvBridge


class ORBFeatureExtractor(Node):

    def __init__(self):

        super().__init__('orb_feature_extractor')

        self.bridge = CvBridge()

        self.orb = cv2.ORB_create(
            nfeatures=500
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

        keypoints, descriptors = self.orb.detectAndCompute(
            gray,
            None
        )

        output = cv2.drawKeypoints(
            frame,
            keypoints,
            None
        )

        cv2.imshow(
            "ORB Features",
            output
        )

        cv2.waitKey(1)


def main(args=None):

    rclpy.init(args=args)

    node = ORBFeatureExtractor()

    rclpy.spin(node)

    node.destroy_node()

    cv2.destroyAllWindows()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
