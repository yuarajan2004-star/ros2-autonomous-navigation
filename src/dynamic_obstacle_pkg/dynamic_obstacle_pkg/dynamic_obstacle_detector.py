#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseArray, Pose


class DynamicObstacleDetector(Node):

    def __init__(self):
        super().__init__('dynamic_obstacle_detector')

        self.previous_ranges = None

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.obstacle_pub = self.create_publisher(
            PoseArray,
            '/dynamic_obstacles',
            10
        )

        self.threshold = 0.30

        self.get_logger().info(
            'Dynamic Obstacle Detector Started'
        )

    def scan_callback(self, msg):

        if self.previous_ranges is None:
            self.previous_ranges = list(msg.ranges)
            return

        obstacle_array = PoseArray()
        obstacle_array.header = msg.header

        angle = msg.angle_min

        for current, previous in zip(
                msg.ranges,
                self.previous_ranges):

            if (
                math.isfinite(current)
                and math.isfinite(previous)
            ):

                if abs(current - previous) > self.threshold:

                    pose = Pose()

                    pose.position.x = (
                        current * math.cos(angle)
                    )

                    pose.position.y = (
                        current * math.sin(angle)
                    )

                    pose.position.z = 0.0

                    obstacle_array.poses.append(pose)

            angle += msg.angle_increment

        self.obstacle_pub.publish(
            obstacle_array
        )

        self.previous_ranges = list(msg.ranges)


def main(args=None):

    rclpy.init(args=args)

    node = DynamicObstacleDetector()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
