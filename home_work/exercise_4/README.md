# exercise no 04: 
## Evolve the robots with the original reward functions and then compare the behavior of
robots evolved with the original and revised reward functions, e.g. in the case of the hopper and
halfcheetah. Could you explain why the original rewards functions are not suitable for evolutionary
strategies ?
* the solution for the exercise is as below
> Describe the difference between the two functions. Describe how the behaviour of the evolved robots differ. 
Reward function of original of original file is has following description:
* alive - to check the the robot that it is fall or stand by checking the height of the robot.
* progress - measure the difference of potntial , it shows the movement to the target.
* electricity_cost -  a cost against the motors, and to be  tuned against the reward
* joints_at_limit_cost -  if joints of the robot stuck anywhere its calculate the palenty for it. 
* feet_collision_cost - this function used to caalculate free falling
these parameter are separately calculate for easch class of the robot
The robot_loclomotors.py function is able to calculate states, apply actions, calculete alive bonuses and rewards, etc for each type of robot.

modified file has folllowing changes with orignal one :
* it has normalize  progress function between [-1, 1]
* alive bonus is changed time time . 
* feet_cost and feet_collision_cost - its calculate the whether robot feet touch the ground or not,
* angle_offset_cost - it is calculation of angle offset between the robot and the target.
Reward function is changed for each type of robot.

# training and testing for orinal and modified files
1. Use commands to build the net in the ./lib directory:
``` bash
python3 setupevonet.py build_ext --inplace
cp net*.so ../bin # or cp net*.dll ../bin
```
2. for traing the robot with orignal and modified files

``` bash
python3 ../bin/es.py -f halfcheetah.ini -s 1
```
python3 ../bin/es.py -f hopper.ini -s 4
```
3.testing the robot behavior
``` bash
python3 ../bin/es.py -f halfcheetah.ini  -t bestgS1
python3 ../bin/es.py -f HOPPER.ini  -t bestgS4

# Result for both files 
*i have test the robot (halfcheetah and hopper) for both orignal and modified files ,in case of orignal rewards fucntion robot didn't move toward the target, its stucked or fall down , robot didn't able to move the correctly,
* in case fo the modified function robot is able to move properly towards the desired target

* Original function are suitable for only reinforcement method, which is working with only one agent,so its didn't help the robot to move towards the target

*Modified function produce the good results for  evolutionary strategies. There is some  additional information like changes in alive bonus estimation, angle calculation from body to target, feet contact with ground, and some other feautre which help the robot to move  correctly toward the target point, so thats why modified function is better for the evolutionary algorithms






 


