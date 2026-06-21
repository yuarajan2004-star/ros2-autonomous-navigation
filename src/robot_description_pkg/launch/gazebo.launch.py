from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    package_dir = get_package_share_directory(
        'robot_description_pkg'
    )

    world_file = os.path.join(
        package_dir,
        'worlds',
        'empty.sdf'
    )

    model_file = os.path.join(
        package_dir,
        'models',
        'mobile_robot',
        'mobile_robot.sdf'
    )

    bridge_launch = os.path.join(
        package_dir,
        'launch',
        'bridge.launch.py'
    )

    gazebo = ExecuteProcess(
        cmd=[
            'gz',
            'sim',
            '-r',
            world_file
        ],
        output='screen'
    )

    spawn_robot = TimerAction(
        period=5.0,
        actions=[
            ExecuteProcess(
                cmd=[
                    'gz',
                    'service',
                    '-s',
                    '/world/empty_world/create',
                    '--reqtype',
                    'gz.msgs.EntityFactory',
                    '--reptype',
                    'gz.msgs.Boolean',
                    '--timeout',
                    '3000',
                    '--req',
                    f'sdf_filename: "{model_file}"'
                ],
                output='screen'
            )
        ]
    )

    bridge = TimerAction(
        period=8.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    bridge_launch
                )
            )
        ]
    )

    return LaunchDescription([
        gazebo,
        spawn_robot,
        bridge
    ])
