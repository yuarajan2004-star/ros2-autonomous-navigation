from setuptools import setup

package_name = 'dynamic_obstacle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=[
        'setuptools'
    ],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.com',
    description='Dynamic obstacle detection tracking semantic mapping and vision navigation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_obstacle_detector = dynamic_obstacle_pkg.dynamic_obstacle_detector:main',
            'obstacle_tracker = dynamic_obstacle_pkg.obstacle_tracker:main',
            'kalman_tracker = dynamic_obstacle_pkg.kalman_tracker:main',
            'multi_object_tracker = dynamic_obstacle_pkg.multi_object_tracker:main',
            'semantic_mapper = dynamic_obstacle_pkg.semantic_mapper:main',
            'vision_navigation = dynamic_obstacle_pkg.vision_navigation:main',
        ],
    },
)
