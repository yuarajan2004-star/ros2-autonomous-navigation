# Installation Guide

## System Requirements

### Operating System

- Ubuntu 24.04 LTS

### ROS Distribution

- ROS2 Jazzy

### Simulator

- Gazebo Harmonic

### Recommended Hardware

- 8 GB RAM minimum
- 16 GB RAM recommended
- Intel i5 / Ryzen 5 or better

---

# Install ROS2 Jazzy

```bash
sudo apt update
sudo apt install software-properties-common -y

sudo add-apt-repository universe -y

sudo apt update

sudo apt install curl -y

sudo curl -sSL \
https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
-o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

sudo apt update

sudo apt install ros-jazzy-desktop -y
```

---

# Install Gazebo Harmonic

```bash
sudo apt install ros-jazzy-ros-gz -y
```

---

# Install Development Tools

```bash
sudo apt install \
python3-colcon-common-extensions \
python3-rosdep \
python3-vcstool \
git \
tree \
-y
```

---

# Initialize rosdep

```bash
sudo rosdep init

rosdep update
```

---

# Clone Repository

```bash
mkdir -p ~/ros2_ws/src

cd ~/ros2_ws/src

git clone <YOUR_REPOSITORY_URL>
```

---

# Install Dependencies

```bash
cd ~/ros2_ws

source /opt/ros/jazzy/setup.bash

rosdep install \
--from-paths src \
--ignore-src \
-r \
-y
```

---

# Build Workspace

```bash
cd ~/ros2_ws

colcon build --symlink-install
```

---

# Source Workspace

```bash
source /opt/ros/jazzy/setup.bash

source ~/ros2_ws/install/setup.bash
```

---

# Verify Installation

List packages:

```bash
ros2 pkg list | grep autonav
```

Expected packages:

```text
autonav_bringup
autonav_control
autonav_costmap
autonav_global_planner
autonav_local_planner
autonav_localization
autonav_planning
autonav_slam
...
```

---

# Launch Example

```bash
ros2 launch autonav_bringup bringup.launch.py
```

---

# Visualization

Open RViz:

```bash
rviz2
```

Add:

- Map
- TF
- LaserScan
- RobotModel
- Path

---

# Simulation

Launch Gazebo:

```bash
ros2 launch robot_description_pkg gazebo.launch.py
```

---

# Troubleshooting

## Workspace Not Found

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

---

## Package Not Found

```bash
colcon build --symlink-install
```

---

## Gazebo Fails To Start

Verify:

```bash
gz sim --version
```

---

## Check ROS Graph

```bash
ros2 node list

ros2 topic list

ros2 service list
```
