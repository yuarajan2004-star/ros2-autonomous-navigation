import rclpy
import numpy as np

from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid


class InflationLayer(Node):

    def __init__(self):

        super().__init__('inflation_layer')

        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        self.publisher = self.create_publisher(
            OccupancyGrid,
            '/inflated_map',
            10
        )

        self.inflation_radius = 4

    def map_callback(self, msg):

        width = msg.info.width
        height = msg.info.height

        data = np.array(
            msg.data,
            dtype=np.int16
        ).reshape(
            (height, width)
        )

        inflated = data.copy()

        obstacle_cells = np.argwhere(data > 50)

        for row, col in obstacle_cells:

            for dx in range(
                -self.inflation_radius,
                self.inflation_radius + 1
            ):
                for dy in range(
                    -self.inflation_radius,
                    self.inflation_radius + 1
                ):

                    nx = row + dx
                    ny = col + dy

                    if (
                        0 <= nx < height and
                        0 <= ny < width
                    ):
                        if inflated[nx, ny] == 0:
                            inflated[nx, ny] = 50

        output = OccupancyGrid()

        output.header = msg.header
        output.info = msg.info
        output.data = inflated.flatten().tolist()

        self.publisher.publish(output)


def main(args=None):

    rclpy.init(args=args)

    node = InflationLayer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
