import rclpy
from rclpy.node import Node

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Pose2D


class RobotMarker(Node):

    def __init__(self):

        super().__init__('robot_marker')

        self.marker_pub = self.create_publisher(
            Marker,
            '/robot_marker',
            10
        )

        self.create_subscription(
            Pose2D,
            '/robot_pose',
            self.pose_callback,
            10
        )

    def pose_callback(self, pose):

        marker = Marker()

        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = "robot"
        marker.id = 0

        marker.type = Marker.ARROW
        marker.action = Marker.ADD

        marker.pose.position.x = pose.x
        marker.pose.position.y = pose.y
        marker.pose.position.z = 0.0

        marker.pose.orientation.w = 1.0

        marker.scale.x = 0.5
        marker.scale.y = 0.15
        marker.scale.z = 0.15

        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0

        self.marker_pub.publish(marker)


def main(args=None):

    rclpy.init(args=args)

    node = RobotMarker()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()