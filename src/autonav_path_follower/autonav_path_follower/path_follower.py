import math

import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped

from nav_msgs.msg import Odometry


class PathFollower(Node):

    def __init__(self):

        super().__init__('path_follower')

        self.goal_x = None
        self.goal_y = None

        self.robot_x = 0.0
        self.robot_y = 0.0

        self.goal_tolerance = 0.2

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.goal_sub = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_callback,
            10
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.get_logger().info(
            'Path follower started'
        )

    def goal_callback(self, msg):

        self.goal_x = msg.pose.position.x
        self.goal_y = msg.pose.position.y

        self.get_logger().info(
            f'New goal: ({self.goal_x:.2f}, {self.goal_y:.2f})'
        )

    def odom_callback(self, msg):

        self.robot_x = msg.pose.pose.position.x
        self.robot_y = msg.pose.pose.position.y

    def control_loop(self):

        if self.goal_x is None:
            return

        dx = self.goal_x - self.robot_x
        dy = self.goal_y - self.robot_y

        distance = math.sqrt(
            dx * dx +
            dy * dy
        )

        cmd = Twist()

        if distance < self.goal_tolerance:

            self.cmd_pub.publish(cmd)

            self.get_logger().info(
                'Goal reached'
            )

            self.goal_x = None
            self.goal_y = None

            return

        cmd.linear.x = min(
            0.3,
            distance
        )

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = PathFollower()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
