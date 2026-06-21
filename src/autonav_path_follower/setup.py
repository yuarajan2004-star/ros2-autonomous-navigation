from setuptools import setup

package_name = 'autonav_path_follower'

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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan.2004@gmail.com',
    description='Path follower',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'path_follower = autonav_path_follower.path_follower:main',
        ],
    },
)
