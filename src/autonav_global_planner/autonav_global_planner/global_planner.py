import rclpy
import math

from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped


class GlobalPlanner(Node):

    def __init__(self):

        super().__init__('global_planner')

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        self.path_pub = self.create_publisher(
            Path,
            '/nav_path',
            10
        )

        self.map_received = False

    def map_callback(self, msg):

        if self.map_received:
            return

        self.map_received = True

        path = Path()

        path.header.frame_id = 'map'

        for i in range(20):

            pose = PoseStamped()

            pose.header.frame_id = 'map'

            pose.pose.position.x = i * 0.2
            pose.pose.position.y = 0.0
            pose.pose.position.z = 0.0

            pose.pose.orientation.w = 1.0

            path.poses.append(pose)

        self.path_pub.publish(path)

        self.get_logger().info(
            f'Published path with {len(path.poses)} waypoints'
        )


def main(args=None):

    rclpy.init(args=args)

    node = GlobalPlanner()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
