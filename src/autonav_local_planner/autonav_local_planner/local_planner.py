import rclpy
import math

from rclpy.node import Node

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class LocalPlanner(Node):

    def __init__(self):

        super().__init__('local_planner')

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.front_distance = 10.0

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

    def odom_callback(self, msg):
        pass

    def scan_callback(self, msg):

        if len(msg.ranges) == 0:
            return

        center_index = len(msg.ranges) // 2

        self.front_distance = msg.ranges[center_index]

    def control_loop(self):

        cmd = Twist()

        if self.front_distance < 0.8:

            cmd.linear.x = 0.0
            cmd.angular.z = 0.5

        else:

            cmd.linear.x = 0.2
            cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)


def main(args=None):

    rclpy.init(args=args)

    node = LocalPlanner()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
