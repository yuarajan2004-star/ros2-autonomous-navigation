import rclpy
from rclpy.node import Node

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

from autonav_planning.astar_search import astar


class AStarPlanner(Node):

    def __init__(self):

        super().__init__('astar_planner')

        self.pub = self.create_publisher(
            Path,
            '/planned_path',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_path
        )

    def publish_path(self):

        # Create occupancy grid
        grid = [[0] * 100 for _ in range(100)]

        # Vertical wall obstacle
        for i in range(20, 80):
            grid[i][50] = 1

        # Run A*
        path_cells = astar(
            grid,
            (10, 10),
            (90, 90)
        )

        # ROS Path message
        path_msg = Path()

        path_msg.header.frame_id = "map"

        for row, col in path_cells:

            pose = PoseStamped()

            pose.header.frame_id = "map"

            # Convert grid cell → world coordinates
            pose.pose.position.x = row * 0.1
            pose.pose.position.y = col * 0.1
            pose.pose.position.z = 0.0

            pose.pose.orientation.w = 1.0

            path_msg.poses.append(pose)

        self.pub.publish(path_msg)

        self.get_logger().info(
            f'Published A* path with {len(path_msg.poses)} points'
        )


def main(args=None):

    rclpy.init(args=args)

    node = AStarPlanner()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()