from robot_control_class import RobotControl

def get_highest_lowest():
    a=0
    b=0
    z=0
    max =0
    min=9999999
    rc=RobotControl()
    list1=rc.get_laser_full()
    for i in list1:
        if i>max and type(i)==float :
            max=i
            a=z+1
            while list1[a]>20:
                a=a-1 
        if i<min and type(i)==float :
            min=i
            b=z+1
        z=z+1
    list2=[a,b]
    print(a,b)
    return list2
