import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D

import math

class EKFNode(Node):

    def __init__(self):

        super().__init__('ekf_node')

        self.publisher_ = self.create_publisher(
            Pose2D,
            '/robot_pose',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_pose
        )

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.get_logger().info(
            'EKF Node Started'
        )

    def publish_pose(self):

        self.x += 0.05
        self.y += 0.03
        self.theta += 0.01

        msg = Pose2D()

        msg.x = self.x
        msg.y = self.y
        msg.theta = self.theta

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'x={msg.x:.2f}, '
            f'y={msg.y:.2f}, '
            f'theta={msg.theta:.2f}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = EKFNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()