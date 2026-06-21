# System Architecture

## End-to-End Data Flow

```text
                         ┌─────────────────┐
                         │ Camera Sensors  │
                         └────────┬────────┘
                                  │
                                  ▼
                      ┌──────────────────────┐
                      │ Visual Odometry      │
                      └────────┬─────────────┘
                               │
                               ▼

┌──────────┐         ┌──────────────────────┐
│   IMU    │────────▶│                      │
└──────────┘         │  EKF Localization    │
                     │                      │
┌──────────┐────────▶│                      │
│ Wheel    │         └──────────┬───────────┘
│ Odometry │                    │
└──────────┘                    ▼

                     ┌──────────────────────┐
                     │      TF Tree         │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │      SLAM            │
                     │ Mapping + Loop       │
                     │ Closure + GraphSLAM  │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │ Occupancy Grid Map   │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │ Global Planner (A*)  │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │ Local Planner        │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │ Pure Pursuit Control │
                     └──────────┬───────────┘
                                │
                                ▼

                     ┌──────────────────────┐
                     │ Differential Drive   │
                     │ Robot                │
                     └──────────────────────┘


Dynamic Obstacle Pipeline

LaserScan / Vision
         │
         ▼
Dynamic Obstacle Detection
         │
         ▼
Kalman Tracking
         │
         ▼
Multi Object Tracking
         │
         ▼
Costmap Update
         │
         ▼
Planner Replanning
```

---

## ROS2 Package Dependency View

```text
autonav_bringup
│
├── autonav_localization
│
├── autonav_slam
│
├── autonav_planning
│
├── autonav_costmap
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
├── robot_description_pkg
│
├── odometry_pkg
│
├── imu_pkg
│
├── slam_benchmark_pkg
│
├── kitti_eval_pkg
│
└── research_report_pkg
```

---

## Research Components

- Dynamic Obstacle Detection
- Kalman Tracking
- Multi-Object Tracking
- Sensor Fusion Optimization
- SLAM Benchmarking
- KITTI Dataset Evaluation
- Research Report Generation

---

## Simulation Components

- Gazebo Harmonic
- RViz2
- ROS2 Jazzy
- Robot State Publisher
- TF Framework
- Sensor Simulation

---

## Outputs

- Localization
- Mapping
- Autonomous Navigation
- Dynamic Replanning
- SLAM Metrics
- KITTI Metrics
- Research Evaluation Results
