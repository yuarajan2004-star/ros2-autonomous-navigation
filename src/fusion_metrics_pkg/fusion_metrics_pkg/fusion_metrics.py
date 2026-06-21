#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image


class FusionMetrics(Node):

    def __init__(self):

        super().__init__('fusion_metrics')

        self.odom_count = 0
        self.scan_count = 0
        self.image_count = 0

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.timer = self.create_timer(
            5.0,
            self.report
        )

    def odom_callback(self, msg):
        self.odom_count += 1

    def scan_callback(self, msg):
        self.scan_count += 1

    def image_callback(self, msg):
        self.image_count += 1

    def report(self):

        self.get_logger().info(
            f'ODOM={self.odom_count} '
            f'SCAN={self.scan_count} '
            f'IMAGE={self.image_count}'
        )

        self.odom_count = 0
        self.scan_count = 0
        self.image_count = 0


def main(args=None):

    rclpy.init(args=args)

    node = FusionMetrics()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
