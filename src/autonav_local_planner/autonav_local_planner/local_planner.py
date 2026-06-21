import rclpy

from rclpy.node import Node

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


class LocalPlanner(Node):

    def __init__(self):

        super().__init__('local_planner')

        self.declare_parameter(
            'forward_speed',
            0.2
        )

        self.declare_parameter(
            'turn_speed',
            0.5
        )

        self.declare_parameter(
            'obstacle_distance_threshold',
            0.8
        )

        self.forward_speed = self.get_parameter(
            'forward_speed'
        ).value

        self.turn_speed = self.get_parameter(
            'turn_speed'
        ).value

        self.obstacle_threshold = self.get_parameter(
            'obstacle_distance_threshold'
        ).value

        self.front_distance = 10.0

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

        self.timer = self.create_timer(
            0.1,
            self.control_loop
        )

        self.get_logger().info(
            f'forward_speed={self.forward_speed}, '
            f'turn_speed={self.turn_speed}, '
            f'obstacle_threshold={self.obstacle_threshold}'
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

        if self.front_distance < self.obstacle_threshold:

            cmd.linear.x = 0.0
            cmd.angular.z = self.turn_speed

        else:

            cmd.linear.x = self.forward_speed
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
