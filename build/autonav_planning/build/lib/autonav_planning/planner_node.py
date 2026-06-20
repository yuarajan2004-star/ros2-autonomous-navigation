import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class PlannerNode(Node):

    def __init__(self):

        super().__init__('planner_node')

        self.publisher_ = self.create_publisher(
            String,
            '/planned_path',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_path
        )

        self.get_logger().info(
            'Planner Node Started'
        )

    def publish_path(self):

        msg = String()

        msg.data = (
            "(0,0)->(1,1)->(2,2)->(3,3)"
        )

        self.publisher_.publish(msg)

def main(args=None):

    rclpy.init(args=args)

    node = PlannerNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()