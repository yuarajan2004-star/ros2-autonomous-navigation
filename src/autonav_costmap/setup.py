from setuptools import setup

package_name = 'autonav_costmap'

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
    install_requires=[
        'setuptools',
        'numpy'
    ],
    zip_safe=True,
    maintainer='yuarajan_s',
    maintainer_email='yuarajan.2004@gmail.com',
    description='Costmap and inflation layer package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'inflation_layer = autonav_costmap.inflation_layer:main',
        ],
    },
)
