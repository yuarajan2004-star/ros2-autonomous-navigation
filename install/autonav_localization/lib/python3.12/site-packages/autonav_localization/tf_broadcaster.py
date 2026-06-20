import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import TransformStamped

from tf2_ros import TransformBroadcaster


class TFBroadcaster(Node):

    def __init__(self):

        super().__init__('tf_broadcaster')

        self.br = TransformBroadcaster(self)

        self.create_subscription(
            Pose2D,
            '/robot_pose',
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):

        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()

        t.header.frame_id = "map"
        t.child_frame_id = "base_link"

        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0

        t.transform.rotation.z = math.sin(msg.theta / 2.0)
        t.transform.rotation.w = math.cos(msg.theta / 2.0)

        self.br.sendTransform(t)


def main(args=None):

    rclpy.init(args=args)

    node = TFBroadcaster()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()