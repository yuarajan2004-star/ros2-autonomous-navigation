#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseArray


class KalmanTracker(Node):

    def __init__(self):
        super().__init__('kalman_tracker')

        self.subscription = self.create_subscription(
            PoseArray,
            '/dynamic_obstacles',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            PoseArray,
            '/tracked_obstacles',
            10
        )

        self.initialized = False

        self.alpha = 0.7

        self.filtered_positions = []

        self.get_logger().info(
            'Kalman Tracker Started'
        )

    def callback(self, msg):

        if not self.initialized:

            self.filtered_positions = [
                [p.position.x, p.position.y]
                for p in msg.poses
            ]

            self.initialized = True

        else:

            count = min(
                len(self.filtered_positions),
                len(msg.poses)
            )

            for i in range(count):

                mx = msg.poses[i].position.x
                my = msg.poses[i].position.y

                self.filtered_positions[i][0] = (
                    self.alpha * self.filtered_positions[i][0]
                    + (1.0 - self.alpha) * mx
                )

                self.filtered_positions[i][1] = (
                    self.alpha * self.filtered_positions[i][1]
                    + (1.0 - self.alpha) * my
                )

        output = PoseArray()
        output.header = msg.header

        count = min(
            len(self.filtered_positions),
            len(msg.poses)
        )

        for i in range(count):

            pose = msg.poses[i]

            pose.position.x = (
                self.filtered_positions[i][0]
            )

            pose.position.y = (
                self.filtered_positions[i][1]
            )

            output.poses.append(pose)

        self.publisher.publish(output)


def main(args=None):

    rclpy.init(args=args)

    node = KalmanTracker()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
