from setuptools import setup
from glob import glob

package_name = 'autonav_bringup'

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
            'share/' + package_name + '/launch',
            glob('launch/*.py')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan.2004@gmail.com',
    description='Autonomous navigation bringup',
    license='Apache-2.0',
    entry_points={},
)
