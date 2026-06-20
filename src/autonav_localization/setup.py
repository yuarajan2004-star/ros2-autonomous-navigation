from setuptools import find_packages, setup

package_name = 'autonav_localization'

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
    'ekf_node = autonav_localization.ekf_node:main',
    'ekf_localization_node = autonav_localization.ekf_localization_node:main',
    'path_publisher = autonav_localization.path_publisher:main',
    'robot_marker = autonav_localization.robot_marker:main',
    'tf_broadcaster = autonav_localization.tf_broadcaster:main',
    ],
},
)
