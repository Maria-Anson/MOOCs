#!/bin/bash

cd /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam
rm /home/user/catkin_ws/src/linux_exam/this/is/my/linux/exam/*
touch exam{1..3}.py
chmod 754 exam1.py
chmod 501 exam2.py
chmod 241 exam3.py
