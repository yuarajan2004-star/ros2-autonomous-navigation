#!/usr/bin/env python3

import rclpy

from rclpy.node import Node
from nav_msgs.msg import Odometry


class GraphSLAMBackend(Node):

    def __init__(self):

        super().__init__('graph_slam_backend')

        self.graph_nodes = []
        self.graph_edges = []

        self.sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        node_id = len(self.graph_nodes)

        self.graph_nodes.append(
            {
                'id': node_id,
                'x': x,
                'y': y
            }
        )

        if node_id > 0:

            self.graph_edges.append(
                {
                    'from': node_id - 1,
                    'to': node_id
                }
            )

        self.get_logger().info(
            f'Graph Nodes={len(self.graph_nodes)} '
            f'Graph Edges={len(self.graph_edges)}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = GraphSLAMBackend()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
