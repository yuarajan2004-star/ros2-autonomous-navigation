from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_dir = get_package_share_directory(
        'robot_description_pkg'
    )

    slam_params = os.path.join(
        package_dir,
        'config',
        'slam.yaml'
    )

    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params
        ]
    )

    return LaunchDescription([
        slam_toolbox_node
    ])
