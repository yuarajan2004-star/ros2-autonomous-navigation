from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    robot_pkg = get_package_share_directory(
        'robot_description_pkg'
    )

    gazebo_launch = os.path.join(
        robot_pkg,
        'launch',
        'gazebo.launch.py'
    )

    bridge_launch = os.path.join(
        robot_pkg,
        'launch',
        'bridge.launch.py'
    )

    tf_launch = os.path.join(
        robot_pkg,
        'launch',
        'full_tf.launch.py'
    )

    slam_launch = os.path.join(
        robot_pkg,
        'launch',
        'slam.launch.py'
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                gazebo_launch
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                bridge_launch
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                tf_launch
            )
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                slam_launch
            )
        ),

        Node(
            package='odometry_pkg',
            executable='wheel_odometry',
            output='screen'
        ),

        Node(
            package='autonav_localization',
            executable='ekf_localization_node',
            output='screen'
        ),

        Node(
            package='autonav_localization',
            executable='tf_broadcaster',
            output='screen'
        ),

        Node(
            package='autonav_planning',
            executable='astar_planner',
            output='screen'
        ),

        Node(
            package='autonav_planning',
            executable='goal_manager',
            output='screen'
        ),

        Node(
            package='autonav_control',
            executable='pure_pursuit',
            output='screen'
        )
    ])
