#!/usr/bin/env python3

import rclpy

from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


class LandmarkCovariance(Node):

    def __init__(self):

        super().__init__('landmark_covariance')

        self.pub = self.create_publisher(
            Marker,
            '/landmark_covariance',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_covariance
        )

    def publish_covariance(self):

        marker = Marker()

        marker.header.frame_id = "base_link"

        marker.ns = "covariance"

        marker.id = 0

        marker.type = Marker.SPHERE

        marker.action = Marker.ADD

        marker.pose.position.x = 2.0
        marker.pose.position.y = 1.0
        marker.pose.position.z = 0.0

        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.1

        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 0.5

        self.pub.publish(marker)


def main(args=None):

    rclpy.init(args=args)

    node = LandmarkCovariance()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
