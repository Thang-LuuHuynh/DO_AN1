import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/thang/NCKH/BSMC--WMR-main/ros2_ws/install/amr_control'
