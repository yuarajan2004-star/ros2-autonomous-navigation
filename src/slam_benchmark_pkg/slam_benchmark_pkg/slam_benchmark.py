#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry


class SlamBenchmark(Node):

    def __init__(self):

        super().__init__('slam_benchmark')

        self.map_updates = 0
        self.odom_updates = 0

        self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(
            10.0,
            self.report
        )

    def map_callback(self, msg):
        self.map_updates += 1

    def odom_callback(self, msg):
        self.odom_updates += 1

    def report(self):

        self.get_logger().info(
            f'MAP_UPDATES={self.map_updates} '
            f'ODOM_UPDATES={self.odom_updates}'
        )

        self.map_updates = 0
        self.odom_updates = 0


def main(args=None):

    rclpy.init(args=args)

    node = SlamBenchmark()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
