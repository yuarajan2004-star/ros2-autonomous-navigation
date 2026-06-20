from setuptools import find_packages, setup

package_name = 'slam_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan_s@todo.todo',
    description='SLAM package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'landmark_detector = slam_pkg.landmark_detector:main',
            'data_association = slam_pkg.data_association:main',
            'ekf_slam = slam_pkg.ekf_slam:main',
            'landmark_covariance = slam_pkg.landmark_covariance:main',
            'occupancy_grid_slam = slam_pkg.occupancy_grid_slam:main',
            'loop_closure = slam_pkg.loop_closure:main',
            'pose_graph = slam_pkg.pose_graph:main',
            'graph_slam_backend = slam_pkg.graph_slam_backend:main',
            'slam_metrics = slam_pkg.slam_metrics:main',
        ],
    },
)
