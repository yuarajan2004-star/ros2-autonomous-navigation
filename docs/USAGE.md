# Usage Guide

## Workspace Setup

Open a terminal:

```bash
cd ~/ros2_ws

source /opt/ros/jazzy/setup.bash

source install/setup.bash
```

---

# System Overview

This project supports:

- Robot Modeling
- Localization
- Visual Odometry
- SLAM
- Navigation
- Dynamic Obstacle Tracking
- Sensor Fusion
- Gazebo Simulation
- KITTI Evaluation
- Research Benchmarking

---

# Robot Visualization

Launch robot model:

```bash
ros2 launch robot_description_pkg display_robot.launch.py
```

Open RViz:

```bash
rviz2
```

Expected:

- Robot Model
- TF Tree
- Sensor Frames

---

# Gazebo Simulation

Launch simulation:

```bash
ros2 launch robot_description_pkg gazebo.launch.py
```

Verify:

```bash
ros2 topic list
```

Expected topics include:

```text
/scan
/tf
/tf_static
/joint_states
```

---

# Localization

Launch EKF Localization:

```bash
ros2 run autonav_localization ekf_localization_node
```

Monitor:

```bash
ros2 topic echo /odom
```

Verify TF:

```bash
ros2 run tf2_tools view_frames
```

---

# Visual Odometry

Launch stereo camera:

```bash
ros2 run visual_odometry_pkg stereo_camera_publisher
```

Launch visual odometry:

```bash
ros2 run visual_odometry_pkg monocular_visual_odometry
```

Verify:

```bash
ros2 topic list | grep pose
```

---

# SLAM

Launch SLAM:

```bash
ros2 launch robot_description_pkg slam.launch.py
```

Check lifecycle state:

```bash
ros2 lifecycle get /slam_toolbox
```

Expected:

```text
active [3]
```

Monitor map:

```bash
ros2 topic echo /map
```

Save map:

```bash
ros2 run nav2_map_server map_saver_cli -f my_map
```

---

# Navigation

Launch full navigation stack:

```bash
ros2 launch autonav_bringup bringup.launch.py
```

Open RViz:

```bash
rviz2
```

Set goal using:

```text
2D Goal Pose
```

Expected:

```text
Path Generated
Robot Tracks Path
Goal Reached
```

---

# Dynamic Obstacle Detection

Launch perception node:

```bash
ros2 run dynamic_obstacle_pkg dynamic_obstacle_detector
```

Monitor:

```bash
ros2 topic echo /dynamic_obstacles
```

---

# Multi-Object Tracking

Launch tracker:

```bash
ros2 run dynamic_obstacle_pkg multi_object_tracker
```

Monitor:

```bash
ros2 topic echo /tracked_objects
```

---

# Sensor Fusion Metrics

Launch metrics node:

```bash
ros2 run fusion_metrics_pkg fusion_metrics
```

Expected outputs:

- Position Error
- Velocity Error
- Fusion Statistics

---

# SLAM Benchmarking

Launch benchmark:

```bash
ros2 run slam_benchmark_pkg benchmark_runner
```

Generated outputs:

```text
ATE
RPE
Trajectory Error
Mapping Accuracy
```

---

# KITTI Evaluation

Run KITTI evaluation:

```bash
ros2 run kitti_eval_pkg kitti_evaluator
```

Generated metrics:

```text
Translation Error
Rotation Error
Trajectory Accuracy
```

---

# Research Report Generation

Generate report:

```bash
ros2 run research_report_pkg generate_report
```

Outputs:

```text
results/
├── benchmark_results.csv
├── kitti_results.csv
├── fusion_metrics.csv
└── final_report.pdf
```

---

# ROS Graph Inspection

Nodes:

```bash
ros2 node list
```

Topics:

```bash
ros2 topic list
```

Services:

```bash
ros2 service list
```

TF Tree:

```bash
ros2 run tf2_tools view_frames
```

---

# Clean Rebuild

```bash
cd ~/ros2_ws

rm -rf build install log

colcon build --symlink-install

source install/setup.bash
```

---

# Expected Final Capabilities

✅ Localization

✅ Visual Odometry

✅ SLAM

✅ Mapping

✅ Autonomous Navigation

✅ Dynamic Obstacle Tracking

✅ Sensor Fusion

✅ Gazebo Simulation

✅ KITTI Benchmarking

✅ Research Evaluation

✅ End-to-End Robotics Stack
