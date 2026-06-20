import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan

import math


class LaserScanSim(Node):

    def __init__(self):

        super().__init__('laser_scan_sim')

        self.pub = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_scan
        )

    def publish_scan(self):

        scan = LaserScan()

        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = "base_link"

        scan.angle_min = -math.pi
        scan.angle_max = math.pi

        scan.angle_increment = math.pi / 180

        scan.range_min = 0.1
        scan.range_max = 10.0

        scan.ranges = [5.0] * 360

        t = self.get_clock().now().nanoseconds / 1e9

        obstacle_distance = 2.0 + math.sin(t)

        for i in range(170, 190):
            scan.ranges[i] = obstacle_distance

        self.pub.publish(scan)


def main(args=None):

    rclpy.init(args=args)

    node = LaserScanSim()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()