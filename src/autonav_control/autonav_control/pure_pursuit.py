import rclpy
from rclpy.node import Node

from nav_msgs.msg import Path
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist

import math


class PurePursuit(Node):

    def __init__(self):

        super().__init__('pure_pursuit')

        self.path = None
        self.pose = None

        self.create_subscription(
            Path,
            '/planned_path',
            self.path_callback,
            10
        )

        self.create_subscription(
            Pose2D,
            '/robot_pose',
            self.pose_callback,
            10
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

    def path_callback(self, msg):
        self.path = msg

    def pose_callback(self, msg):
        self.pose = msg

    def control_loop(self):

        if self.path is None or self.pose is None:
            return

        target = self.path.poses[min(10, len(self.path.poses)-1)]

        dx = target.pose.position.x - self.pose.x
        dy = target.pose.position.y - self.pose.y

        target_heading = math.atan2(dy, dx)

        error = target_heading - self.pose.theta

        cmd = Twist()

        cmd.linear.x = 0.5
        cmd.angular.z = error

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = PurePursuit()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()