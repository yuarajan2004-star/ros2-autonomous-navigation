import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData

import math


class OccupancyMapper(Node):

    def __init__(self):

        super().__init__('occupancy_mapper')

        self.scan = None

        self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.map_pub = self.create_publisher(
            OccupancyGrid,
            '/scan_map',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_map
        )

    def scan_callback(self, msg):
        self.scan = msg

    def publish_map(self):

        if self.scan is None:
            return

        grid = OccupancyGrid()

        grid.header.frame_id = "base_link"

        grid.info = MapMetaData()

        grid.info.width = 100
        grid.info.height = 100

        grid.info.resolution = 0.1

        grid.info.origin.position.x = -5.0
        grid.info.origin.position.y = -5.0

        data = [0] * (100 * 100)

        angle = self.scan.angle_min

        for r in self.scan.ranges:

            if 0.1 < r < 10.0:

                x = r * math.cos(angle)
                y = r * math.sin(angle)

                gx = int((x + 5.0) / 0.1)
                gy = int((y + 5.0) / 0.1)

                if 0 <= gx < 100 and 0 <= gy < 100:

                    idx = gy * 100 + gx

                    data[idx] = 100

            angle += self.scan.angle_increment

        grid.data = data

        self.map_pub.publish(grid)


def main(args=None):

    rclpy.init(args=args)

    node = OccupancyMapper()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()  