#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseArray


class ObstacleTracker(Node):

    def __init__(self):
        super().__init__('obstacle_tracker')

        self.subscription = self.create_subscription(
            PoseArray,
            '/dynamic_obstacles',
            self.obstacle_callback,
            10
        )

        self.publisher = self.create_publisher(
            PoseArray,
            '/tracked_obstacles',
            10
        )

        self.latest_tracks = PoseArray()

        self.get_logger().info(
            'Obstacle Tracker Started'
        )

    def obstacle_callback(self, msg):

        self.latest_tracks = msg

        self.publisher.publish(
            self.latest_tracks
        )


def main(args=None):

    rclpy.init(args=args)

    node = ObstacleTracker()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
