import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path


class GoalManager(Node):

    def __init__(self):

        super().__init__('goal_manager')

        self.sub = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_callback,
            10
        )

        self.pub = self.create_publisher(
            Path,
            '/goal_path',
            10
        )

    def goal_callback(self, msg):

        goal_x = msg.pose.position.x
        goal_y = msg.pose.position.y

        self.get_logger().info(
            f"Goal received: {goal_x:.2f}, {goal_y:.2f}"
        )

        path = Path()

        path.header.frame_id = "base_link"

        steps = 20

        for i in range(steps + 1):

            pose = PoseStamped()

            pose.header.frame_id = "base_link"

            pose.pose.position.x = goal_x * i / steps
            pose.pose.position.y = goal_y * i / steps

            pose.pose.orientation.w = 1.0

            path.poses.append(pose)

        self.pub.publish(path)


def main(args=None):

    rclpy.init(args=args)

    node = GoalManager()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()