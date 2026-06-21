import rclpy

from rclpy.node import Node

from geometry_msgs.msg import PoseStamped


class GoalManager(Node):

    def __init__(self):

        super().__init__('goal_manager')

        self.goal_sub = self.create_subscription(
            PoseStamped,
            '/goal_pose',
            self.goal_callback,
            10
        )

        self.current_goal = None

        self.get_logger().info(
            'Waiting for goals on /goal_pose'
        )

    def goal_callback(self, msg):

        self.current_goal = msg

        self.get_logger().info(
            f'Goal received: '
            f'x={msg.pose.position.x:.2f}, '
            f'y={msg.pose.position.y:.2f}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = GoalManager()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
