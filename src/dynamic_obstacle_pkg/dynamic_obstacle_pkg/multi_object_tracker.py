#!/usr/bin/env python3

import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseArray


class MultiObjectTracker(Node):

    def __init__(self):
        super().__init__('multi_object_tracker')

        self.subscription = self.create_subscription(
            PoseArray,
            '/dynamic_obstacles',
            self.callback,
            10
        )

        self.publisher = self.create_publisher(
            PoseArray,
            '/multi_object_tracks',
            10
        )

        self.tracks = {}
        self.next_track_id = 0

        self.association_distance = 0.75

        self.get_logger().info(
            'Multi Object Tracker Started'
        )

    def distance(self, x1, y1, x2, y2):
        return math.sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2
        )

    def callback(self, msg):

        for pose in msg.poses:

            px = pose.position.x
            py = pose.position.y

            matched_track = None
            best_distance = float('inf')

            for track_id, track in self.tracks.items():

                d = self.distance(
                    px,
                    py,
                    track['x'],
                    track['y']
                )

                if d < self.association_distance and d < best_distance:
                    matched_track = track_id
                    best_distance = d

            if matched_track is None:

                self.tracks[self.next_track_id] = {
                    'x': px,
                    'y': py
                }

                self.get_logger().info(
                    f'Created Track {self.next_track_id}'
                )

                self.next_track_id += 1

            else:

                self.tracks[matched_track]['x'] = px
                self.tracks[matched_track]['y'] = py

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = MultiObjectTracker()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
