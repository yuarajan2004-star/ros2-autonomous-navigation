from setuptools import find_packages, setup

package_name = 'autonav_planning'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan_s@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'astar_planner = autonav_planning.astar_planner:main',
        'map_publisher = autonav_planning.map_publisher:main',
        'laser_scan_sim = autonav_planning.laser_scan_sim:main',
        'occupancy_mapper = autonav_planning.occupancy_mapper:main',
        'replanner = autonav_planning.replanner:main',
        'goal_manager = autonav_planning.goal_manager:main',
    ],
    },
)
