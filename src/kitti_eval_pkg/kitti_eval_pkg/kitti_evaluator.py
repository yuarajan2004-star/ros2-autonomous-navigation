#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry


class KittiEvaluator(Node):

    def __init__(self):

        super().__init__('kitti_evaluator')

        self.path_length = 0.0

        self.prev_x = None
        self.prev_y = None

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

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if self.prev_x is not None:

            dx = x - self.prev_x
            dy = y - self.prev_y

            self.path_length += math.sqrt(
                dx * dx + dy * dy
            )

        self.prev_x = x
        self.prev_y = y

    def report(self):

        self.get_logger().info(
            f'PATH_LENGTH={self.path_length:.3f} m'
        )


def main(args=None):

    rclpy.init(args=args)

    node = KittiEvaluator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
