import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData


class MapPublisher(Node):

    def __init__(self):

        super().__init__('map_publisher')

        self.pub = self.create_publisher(
            OccupancyGrid,
            '/map',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_map
        )

    def publish_map(self):

        grid = OccupancyGrid()

        grid.header.frame_id = "map"

        grid.info = MapMetaData()

        grid.info.width = 100
        grid.info.height = 100

        grid.info.resolution = 0.1

        grid.info.origin.position.x = 0.0
        grid.info.origin.position.y = 0.0

        data = [0] * (100 * 100)

        for y in range(20, 80):
            data[y * 100 + 50] = 100

        grid.data = data

        self.pub.publish(grid)


def main(args=None):

    rclpy.init(args=args)

    node = MapPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()