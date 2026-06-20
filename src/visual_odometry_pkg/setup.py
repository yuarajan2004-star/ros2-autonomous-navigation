from setuptools import find_packages, setup

package_name = 'visual_odometry_pkg'

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
    description='Visual Odometry Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'visual_odometry = visual_odometry_pkg.visual_odometry:main',
            'orb_feature_extractor = visual_odometry_pkg.orb_feature_extractor:main',
            'feature_matcher = visual_odometry_pkg.feature_matcher:main',
            'ransac_feature_matching = visual_odometry_pkg.ransac_feature_matching:main',
            'essential_matrix_estimator = visual_odometry_pkg.essential_matrix_estimator:main',
            'monocular_visual_odometry = visual_odometry_pkg.monocular_visual_odometry:main',
            'stereo_camera_publisher = visual_odometry_pkg.stereo_camera_publisher:main',
            'stereo_vision = visual_odometry_pkg.stereo_vision:main',
            'depth_estimator = visual_odometry_pkg.depth_estimator:main',
            'visual_place_recognition = visual_odometry_pkg.visual_place_recognition:main',
            'vision_loop_closure = visual_odometry_pkg.vision_loop_closure:main',
            'visual_slam = visual_odometry_pkg.visual_slam:main',
        ],
    },
)
