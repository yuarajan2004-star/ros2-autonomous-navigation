#!/usr/bin/env python3

import cv2

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

from cv_bridge import CvBridge


class VisionNavigation(Node):

    def __init__(self):

        super().__init__('vision_navigation')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.get_logger().info(
            'Vision Navigation Started'
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

        corners = cv2.goodFeaturesToTrack(
            gray,
            maxCorners=50,
            qualityLevel=0.01,
            minDistance=10
        )

        twist = Twist()

        if corners is not None:

            corners = corners.astype(int)

            mean_x = 0

            for corner in corners:
                x, y = corner.ravel()
                mean_x += x

            mean_x /= len(corners)

            image_center = frame.shape[1] / 2

            error = mean_x - image_center

            twist.linear.x = 0.20
            twist.angular.z = -error / 500.0

        self.cmd_pub.publish(twist)


def main(args=None):

    rclpy.init(args=args)

    node = VisionNavigation()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
