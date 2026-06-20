#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Imu


class ImuPublisher(Node):

    def __init__(self):

        super().__init__('imu_publisher')

        self.pub = self.create_publisher(
            Imu,
            '/imu/data',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_imu
        )

        self.yaw = 0.0

    def publish_imu(self):

        self.yaw += 0.01

        msg = Imu()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        msg.orientation.z = math.sin(self.yaw / 2.0)
        msg.orientation.w = math.cos(self.yaw / 2.0)

        self.pub.publish(msg)


def main():

    rclpy.init()

    node = ImuPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
