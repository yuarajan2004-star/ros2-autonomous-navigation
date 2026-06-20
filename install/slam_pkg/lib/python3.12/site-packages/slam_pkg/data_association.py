#!/usr/bin/env python3

import rclpy
import math

from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class DataAssociation(Node):

    def __init__(self):

        super().__init__('data_association')

        self.landmarks = []

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

    def scan_callback(self, msg):

        angle = msg.angle_min

        for r in msg.ranges:

            if math.isfinite(r):

                x = r * math.cos(angle)
                y = r * math.sin(angle)

                matched = False

                for lm in self.landmarks:

                    dist = math.sqrt(
                        (x - lm[0])**2 +
                        (y - lm[1])**2
                    )

                    if dist < 0.5:
                        matched = True
                        break

                if not matched:
                    self.landmarks.append((x, y))

                    self.get_logger().info(
                        f"New Landmark: ({x:.2f}, {y:.2f})"
                    )

            angle += msg.angle_increment


def main(args=None):

    rclpy.init(args=args)

    node = DataAssociation()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
