import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yuarajan_s/ros2_ws/install/visual_odometry_pkg'
