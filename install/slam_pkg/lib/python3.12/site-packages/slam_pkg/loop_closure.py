#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry


class LoopClosure(Node):

    def __init__(self):

        super().__init__('loop_closure')

        self.pose_history = []

        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        current_pose = (x, y)

        for old_pose in self.pose_history:

            dist = math.sqrt(
                (x - old_pose[0]) ** 2 +
                (y - old_pose[1]) ** 2
            )

            if dist < 0.5:

                self.get_logger().info(
                    f'Loop Closure Detected at ({x:.2f}, {y:.2f})'
                )

                break

        self.pose_history.append(current_pose)


def main(args=None):

    rclpy.init(args=args)

    node = LoopClosure()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
