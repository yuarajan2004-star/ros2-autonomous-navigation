import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

import math
import time


class RecoveryBehavior(Node):

    def __init__(self):

        super().__init__('recovery_behavior')

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        self.last_x = None
        self.last_y = None

        self.last_progress_time = time.time()

        self.timer = self.create_timer(
            1.0,
            self.check_stuck
        )

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if self.last_x is None:

            self.last_x = x
            self.last_y = y
            return

        distance = math.sqrt(
            (x - self.last_x) ** 2 +
            (y - self.last_y) ** 2
        )

        if distance > 0.05:

            self.last_progress_time = time.time()

            self.last_x = x
            self.last_y = y

    def check_stuck(self):

        elapsed = time.time() - self.last_progress_time

        if elapsed > 5.0:

            self.get_logger().warn(
                'Robot appears stuck. Executing recovery.'
            )

            self.execute_recovery()

            self.last_progress_time = time.time()

    def execute_recovery(self):

        backup = Twist()
        backup.linear.x = -0.15

        rotate = Twist()
        rotate.angular.z = 0.5

        stop = Twist()

        start = time.time()

        while time.time() - start < 2.0:
            self.cmd_pub.publish(backup)
            time.sleep(0.1)

        start = time.time()

        while time.time() - start < 3.0:
            self.cmd_pub.publish(rotate)
            time.sleep(0.1)

        self.cmd_pub.publish(stop)

        self.get_logger().info(
            'Recovery completed.'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RecoveryBehavior()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
