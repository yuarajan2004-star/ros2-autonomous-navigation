#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion


class VisualOdometry(Node):

    def __init__(self):

        super().__init__('visual_odometry')

        self.pub = self.create_publisher(
            Odometry,
            '/visual_odom',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.update
        )

        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def update(self):

        dt = 0.1

        self.x += 0.18 * math.cos(self.theta) * dt
        self.y += 0.18 * math.sin(self.theta) * dt
        self.theta += 0.04 * dt

        msg = Odometry()

        msg.header.frame_id = "odom"
        msg.child_frame_id = "base_link"

        msg.pose.pose.position.x = self.x
        msg.pose.pose.position.y = self.y

        q = Quaternion()

        q.x = 0.0
        q.y = 0.0
        q.z = math.sin(self.theta / 2.0)
        q.w = math.cos(self.theta / 2.0)

        msg.pose.pose.orientation = q

        self.pub.publish(msg)


def main():

    rclpy.init()

    node = VisualOdometry()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
