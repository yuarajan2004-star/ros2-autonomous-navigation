#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan


class EKFSLAM(Node):

    def __init__(self):

        super().__init__('ekf_slam')

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

        self.landmarks = []

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.create_timer(
            1.0,
            self.status_callback
        )

    def odom_callback(self, msg):

        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

    def scan_callback(self, msg):

        pass

    def status_callback(self):

        self.get_logger().info(
            f"Pose = ({self.x:.2f}, {self.y:.2f}) "
            f"Landmarks = {len(self.landmarks)}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = EKFSLAM()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
