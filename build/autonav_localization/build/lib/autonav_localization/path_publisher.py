import rclpy
from rclpy.node import Node

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose2D


class PathPublisher(Node):

    def __init__(self):

        super().__init__('path_publisher')

        self.path_pub = self.create_publisher(
            Path,
            '/robot_path',
            10
        )

        self.subscription = self.create_subscription(
            Pose2D,
            '/robot_pose',
            self.pose_callback,
            10
        )

        self.path_msg = Path()
        self.path_msg.header.frame_id = "map"

        self.get_logger().info(
            "Path Publisher Started"
        )

    def pose_callback(self, pose):

        pose_stamped = PoseStamped()

        pose_stamped.header.stamp = self.get_clock().now().to_msg()
        pose_stamped.header.frame_id = "map"

        pose_stamped.pose.position.x = pose.x
        pose_stamped.pose.position.y = pose.y
        pose_stamped.pose.position.z = 0.0

        pose_stamped.pose.orientation.w = 1.0

        self.path_msg.header.stamp = (
            self.get_clock().now().to_msg()
        )

        self.path_msg.poses.append(
            pose_stamped
        )

        self.path_pub.publish(
            self.path_msg
        )


def main(args=None):

    rclpy.init(args=args)

    node = PathPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()