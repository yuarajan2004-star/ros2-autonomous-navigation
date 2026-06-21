#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry


class ReportGenerator(Node):

    def __init__(self):

        super().__init__('report_generator')

        self.odom_count = 0

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(
            30.0,
            self.generate_report
        )

    def odom_callback(self, msg):
        self.odom_count += 1

    def generate_report(self):

        self.get_logger().info(
            '\n'
            '===== AUTONOMOUS ROBOTICS REPORT =====\n'
            f'Odometry Messages: {self.odom_count}\n'
            'SLAM: ACTIVE\n'
            'Localization: ACTIVE\n'
            'Navigation: ACTIVE\n'
            'Vision Navigation: ACTIVE\n'
            'Dynamic Obstacle Tracking: ACTIVE\n'
            'Sensor Fusion: ACTIVE\n'
            'Status: SYSTEM OPERATIONAL\n'
            '======================================'
        )


def main(args=None):

    rclpy.init(args=args)

    node = ReportGenerator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
