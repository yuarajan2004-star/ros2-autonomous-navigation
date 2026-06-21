from setuptools import find_packages, setup

package_name = 'autonav_utils'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuarajan',
    maintainer_email='yuarajan@example.com',
    description='Shared utilities for AutoNav',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
