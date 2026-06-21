from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import (
    PythonLaunchDescriptionSource
)

from launch_ros.actions import Node

from ament_index_python.packages import (
    get_package_share_directory
)

import os


def generate_launch_description():

    robot_description_pkg = (
        get_package_share_directory(
            'robot_description_pkg'
        )
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
        )
    )

    inflation_layer = Node(
        package='autonav_costmap',
        executable='inflation_layer',
        output='screen'
    )

    global_planner = Node(
        package='autonav_global_planner',
        executable='global_planner',
        output='screen'
    )

    local_planner = Node(
        package='autonav_local_planner',
        executable='local_planner',
        parameters=[
            os.path.expanduser(
                '~/ros2_ws/src/autonav_local_planner/config/local_planner.yaml'
            )
        ],
        output='screen'
    )

    recovery_behavior = Node(
        package='autonav_recovery',
        executable='recovery_behavior',
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        slam_launch,
        inflation_layer,
        global_planner,
        local_planner,
        recovery_behavior
    ])
