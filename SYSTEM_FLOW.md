# System Flow Diagram

Lidar ──────┐
│
Camera ─────┼──► Localization
│
IMU ────────┘

Localization
│
▼
SLAM
│
▼
Occupancy Map
│
▼
Planner
│
▼
Path Generation
│
▼
Controller
│
▼
cmd_vel
│
▼
Robot Motion
