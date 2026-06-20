#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from nav_msgs.msg import Odometry


class PoseGraph(Node):

    def __init__(self):

        super().__init__('pose_graph')

        self.nodes = []
        self.edges = []

        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        current_node = (x, y)

        node_id = len(self.nodes)

        self.nodes.append(current_node)

        if node_id > 0:

            self.edges.append(
                (
                    node_id - 1,
                    node_id
                )
            )

        self.get_logger().info(
            f'Nodes={len(self.nodes)} '
            f'Edges={len(self.edges)}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = PoseGraph()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
