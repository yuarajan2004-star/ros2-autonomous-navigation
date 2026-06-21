from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    bringup_pkg = get_package_share_directory(
        'autonav_bringup'
    )

    robot_description_pkg = get_package_share_directory(
        'robot_description_pkg'
    )

    params_file = os.path.join(
        bringup_pkg,
        'config',
        'autonav_params.yaml'
    )

    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                robot_description_pkg,
                'launch',
                'gazebo.launch.py'
            )
        )
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                robot_description_pkg,
                'launch',
                'slam.launch.py'
            )
        ),
        launch_arguments={
            'params_file': params_file
        }.items()
    )

    display_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                robot_description_pkg,
                'launch',
                'display_robot.launch.py'
            )
        )
    )

    bridge_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                robot_description_pkg,
                'launch',
                'bridge.launch.py'
            )
        )
    )

    return LaunchDescription([
        gazebo_launch,
        bridge_launch,
        slam_launch,
        display_launch,
    ])
