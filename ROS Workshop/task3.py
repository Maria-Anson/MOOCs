from robot_control_class import RobotControl

class ExamControl:
    def __init__(self):
        self.rc=RobotControl()
    def get_laser_readings(self):
        a=self.rc.get_laser(0)
        b=self.rc.get_laser(719)
        list1=[b,a]
        return list1
    def main(self):
        list2=self.get_laser_readings()
        print(list2[0],list2[1])
        while list2[0]<50 or list2[1]<50 :
            list2=self.get_laser_readings()
            self.rc.move_straight()
        self.rc.stop_robot()
