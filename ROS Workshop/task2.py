from robot_control_class import RobotControl

rc=RobotControl()
con=100
while con>1:
    rc.move_straight()
    con =rc.get_laser(360)
rc.turn('clockwise',0.5,3.0)
