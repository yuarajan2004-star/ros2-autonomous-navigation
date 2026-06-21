# Autonomous Navigation System Architecture

## Overview

This project implements a complete ROS2 autonomous mobile robot stack including:

* Robot Modeling
* Simulation
* Localization
* SLAM
* Planning
* Control
* Navigation
* Software Engineering Infrastructure

---

## System Architecture

Robot Sensors

* IMU
* Lidar
* Camera
* Wheel Encoders

↓

Localization Layer

* Wheel Odometry
* EKF Fusion
* Visual Odometry

↓

SLAM Layer

* Occupancy Grid Mapping
* Loop Closure
* Graph SLAM
* SLAM Toolbox

↓

Planning Layer

* A* Global Planner
* Goal Management
* Path Generation

↓

Control Layer

* Pure Pursuit Controller
* Velocity Generation

↓

Robot Motion

* cmd_vel

---

## ROS2 Package Structure

autonav_bringup

* Launch files
* Configuration files

autonav_description

* URDF
* SDF
* TF tree

autonav_localization

* Odometry
* EKF
* Sensor fusion

autonav_perception

* ORB
* Feature matching
* Visual odometry

autonav_slam

* Mapping
* Loop closure
* Graph SLAM

autonav_planning

* Global planning

autonav_control

* Motion control

autonav_msgs

* Custom interfaces

autonav_utils

* Logging
* Shared utilities

---

## Major Topics

Published

* /odom
* /map
* /goal_path
* /cmd_vel
* /tf

Subscribed

* /scan
* /imu
* /goal_pose

---

## Simulation Environment

* ROS2 Jazzy
* Gazebo Harmonic
* RViz2
* Ubuntu 24.04

---

## Testing Infrastructure

* Unit Testing
* Integration Testing
* Configuration Management
* Logging Framework

---

## Development Workflow

Code

↓

Unit Tests

↓

Integration Tests

↓

Simulation Validation

↓

Git Commit

↓

Deployment
