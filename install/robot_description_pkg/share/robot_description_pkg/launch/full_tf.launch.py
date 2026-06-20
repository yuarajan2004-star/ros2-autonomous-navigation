from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_dir = get_package_share_directory(
        'robot_description_pkg'
    )

    urdf_file = os.path.join(
        package_dir,
        'urdf',
        'mobile_robot.urdf'
    )

    rviz_file = os.path.join(
        package_dir,
        'rviz',
        'robot.rviz'
    )

    with open(urdf_file, 'r') as f:
        robot_description = f.read()

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[
                {'robot_description': robot_description}
            ]
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=[
                '0',
                '0',
                '0',
                '0',
                '0',
                '0',
                'map',
                'odom'
            ]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_file]
        )

    ])
