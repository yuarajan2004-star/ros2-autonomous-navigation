import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped


class Replanner(Node):

    def __init__(self):

        super().__init__('replanner')

        self.sub = self.create_subscription(
            OccupancyGrid,
            '/scan_map',
            self.map_callback,
            10
        )

        self.pub = self.create_publisher(
            Path,
            '/replanned_path',
            10
        )

    def map_callback(self, msg):

        path = Path()

        path.header.frame_id = "base_link"

        waypoints = [
            (0.0, 0.0),
            (1.0, 0.5),
            (2.0, 1.0),
            (3.0, 2.0),
            (4.0, 3.0)
        ]

        for x, y in waypoints:

            pose = PoseStamped()

            pose.header.frame_id = "base_link"

            pose.pose.position.x = x
            pose.pose.position.y = y

            pose.pose.orientation.w = 1.0

            path.poses.append(pose)

        self.pub.publish(path)


def main(args=None):

    rclpy.init(args=args)

    node = Replanner()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()