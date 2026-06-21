from setuptools import setup
from glob import glob

package_name = 'autonav_local_planner'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/config',
            glob('config/*.yaml')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan.2004@gmail.com',
    description='Local planner',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'local_planner = autonav_local_planner.local_planner:main',
        ],
    },
)
