import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist
from nav_msgs.msg import Path


class PathFollower(Node):

    def __init__(self):

        super().__init__('path_follower')

        self.path = None

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

        self.robot_pose = None

    def path_callback(self, msg):
        self.path = msg

    def pose_callback(self, msg):

        self.robot_pose = msg

        if self.path is None:
            return

        goal = self.path.poses[-1]

        dx = goal.pose.position.x - msg.x
        dy = goal.pose.position.y - msg.y

        cmd = Twist()

        cmd.linear.x = 0.5

        cmd.angular.z = 0.2 * dy

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = PathFollower()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()