from setuptools import find_packages, setup

package_name = 'slam_benchmark_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan.2004@gmail.com',
    description='SLAM benchmarking package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'slam_benchmark = slam_benchmark_pkg.slam_benchmark:main',
        ],
    },
)
