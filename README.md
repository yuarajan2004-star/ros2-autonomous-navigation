# ROS2 Autonomous Navigation and SLAM System

## Overview

This project implements a complete autonomous mobile robot software stack using ROS2 Jazzy.

Features include:

- Localization (Wheel Odometry + EKF)
- Visual Odometry
- SLAM
- Navigation
- Costmaps
- Dynamic Obstacle Tracking
- Sensor Fusion
- KITTI Dataset Evaluation
- Gazebo Simulation
- Research Benchmarking

---

# System Architecture

```text
                     +------------------+
                     |  Camera Sensors  |
                     +---------+--------+
                               |
                               v
                 +--------------------------+
                 |  Visual Odometry Module  |
                 +------------+-------------+
                              |
                              v

+---------+        +---------------------+
|   IMU   |------->|                     |
+---------+        |   EKF Localization  |
                   |                     |
+---------+------->|                     |
| Wheel   |        +----------+----------+
| Odom    |                   |
+---------+                   v

                   +----------------------+
                   |      TF System       |
                   +----------+-----------+
                              |
                              v

                     +------------------+
                     |   SLAM Module    |
                     +---------+--------+
                               |
                               v

                     +------------------+
                     | Occupancy Grid   |
                     |      Map         |
                     +---------+--------+
                               |
                               v

                 +--------------------------+
                 | Global Planner (A*)      |
                 +------------+-------------+
                              |
                              v

                 +--------------------------+
                 | Local Planner            |
                 +------------+-------------+
                              |
                              v

                 +--------------------------+
                 | Pure Pursuit Controller  |
                 +------------+-------------+
                              |
                              v

                     +------------------+
                     | Differential     |
                     | Drive Robot      |
                     +------------------+

Dynamic Obstacle Detection
            |
            v
     Multi Object Tracking
            |
            v
       Costmap Updates
            |
            v
     Planner Replanning
```

---

# ROS2 Package Architecture

```text
autonav_bringup
│
├── autonav_localization
│   ├── EKF
│   ├── TF
│   └── Sensor Fusion
│
├── autonav_slam
│   ├── Occupancy Grid Mapping
│   ├── Loop Closure
│   └── Graph SLAM
│
├── autonav_planning
│   ├── A* Planner
│   └── Goal Management
│
├── autonav_costmap
│   ├── Costmap
│   └── Inflation Layer
│
├── autonav_local_planner
│
├── autonav_control
│
├── autonav_perception
│
├── dynamic_obstacle_pkg
│
├── visual_odometry_pkg
│
└── robot_description_pkg
```

---

# Implemented Technologies

- ROS2 Jazzy
- Gazebo Harmonic
- RViz2
- OpenCV
- EKF
- Visual Odometry
- Graph SLAM
- A* Planning
- Costmaps
- Multi Object Tracking
- KITTI Evaluation

---

# Workspace

```bash
ros2_ws
├── src
├── docs
├── screenshots
├── results
├── build
├── install
└── log
```
