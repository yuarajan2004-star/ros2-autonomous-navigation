#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseArray


class SemanticMapper(Node):

    def __init__(self):
        super().__init__('semantic_mapper')

        self.subscription = self.create_subscription(
            PoseArray,
            '/multi_object_tracks',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            PoseArray,
            '/semantic_obstacles',
            10
        )

        self.get_logger().info(
            'Semantic Mapper Started'
        )

    def callback(self, msg):

        semantic_msg = PoseArray()
        semantic_msg.header = msg.header

        for pose in msg.poses:

            x = pose.position.x
            y = pose.position.y

            distance = (x**2 + y**2) ** 0.5

            if distance < 1.5:
                self.get_logger().info(
                    f'Person detected at ({x:.2f}, {y:.2f})'
                )
            elif distance < 3.0:
                self.get_logger().info(
                    f'Chair detected at ({x:.2f}, {y:.2f})'
                )
            else:
                self.get_logger().info(
                    f'Unknown object at ({x:.2f}, {y:.2f})'
                )

            semantic_msg.poses.append(pose)

        self.publisher.publish(semantic_msg)


def main(args=None):

    rclpy.init(args=args)

    node = SemanticMapper()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
