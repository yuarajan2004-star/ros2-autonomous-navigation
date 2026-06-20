#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry


class SLAMMetrics(Node):

    def __init__(self):

        super().__init__('slam_metrics')

        self.pose_history = []

        self.loop_closures = 0

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

                self.loop_closures += 1

                break

        self.pose_history.append(current_pose)

        self.get_logger().info(
            f'Poses={len(self.pose_history)} '
            f'Edges={max(0, len(self.pose_history)-1)} '
            f'LoopClosures={self.loop_closures}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = SLAMMetrics()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
