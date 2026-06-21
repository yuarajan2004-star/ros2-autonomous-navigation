# Autonomous Navigation System Architecture

## Package Layout

autonav_bringup
- Launch files
- Parameter files

autonav_description
- Robot model
- URDF
- SDF
- TF tree

autonav_localization
- Wheel odometry
- EKF
- IMU fusion

autonav_perception
- Visual odometry
- Feature extraction
- Stereo vision

autonav_slam
- SLAM toolbox
- Graph SLAM
- Loop closure

autonav_planning
- A* planner
- Global planning

autonav_control
- Pure pursuit
- Motion control

autonav_msgs
- Custom messages
- Custom services
