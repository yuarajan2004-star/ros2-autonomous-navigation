#!/usr/bin/env python3

import rclpy
import math

from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


class LandmarkDetector(Node):

    def __init__(self):
        super().__init__('landmark_detector')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.marker_pub = self.create_publisher(
            Marker,
            '/landmarks',
            10
        )

    def scan_callback(self, msg):

        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = "landmarks"
        marker.id = 0

        marker.type = Marker.POINTS
        marker.action = Marker.ADD

        marker.scale.x = 0.15
        marker.scale.y = 0.15

        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        angle = msg.angle_min

        for r in msg.ranges:

            if math.isfinite(r):

                p = Point()

                p.x = r * math.cos(angle)
                p.y = r * math.sin(angle)
                p.z = 0.0

                marker.points.append(p)

            angle += msg.angle_increment

        self.marker_pub.publish(marker)


def main(args=None):

    rclpy.init(args=args)

    node = LandmarkDetector()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
