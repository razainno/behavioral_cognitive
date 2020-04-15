# Exercise 6: 
## 

>The source code (discrim.cpp, discrim.h, utilities.cpp, utilities.h, robot-env.cpp, robot-env.h, ErDiscrim.pxd, ErDiscrim.pyx, and setupErDiscrim.py) can be compiled from the ./lib folder with the following instructions:

i have run the following command 

```bash
python3 setupErDiscrim.py build_ext --inplace
cp ErDiscrim*.so ../bin # or cp ErDiscrim*.dll ../bin

The discrim.cpp and discrim.h files include the definition of the gym functions (i.e. env-reset(), env.step(), env.render() ext.) and the calculation of the reward. The robot-env.cpp and robot-env.h files include a series of methods that permit to simulate the translation and rotation movement of the robot in 2D, 
```
# Task
> Run 10 replications of the experiment from the evorobotpy/xdiscrim folder by using different seeds. 
To launch the training process go to the ./xdiscrim directory and use the following command:
``` bash
python3 ../bin/es.py -f ErDiscrim.ini -s (seed_number)
```
I used this sequence of seeds: ,, 7, 8, 9, 10, 15, 19, 28,98 I uploaded all files with results.
> Test and analyze the strategy displayed by best robot of each replication. Describe the strategies of the robots by grouping them in families. Try to explain why the robot of each family behave in that manner. 

I noticed 3 different behavior of this  robot:
* 1. Seeds 1, 5, 7, 8, 10. Robot moves to the target, then quickly go toward target and stopped to near it
![Alt text](https://github.com/razainno/behavioral_cognitive/blob/master/home_work/exercise_6/3.gif "The robot gets stucked near the target")
* 2. Seeds 15. Robot moves to the target and then start to move around the target.
![Alt text](https://github.com/razainno/behavioral_cognitive/blob/master/home_work/exercise_6/2.gif "The robot gets stucked near the target")
* 3. Seed 19. Robot moves to the target and then  rotates around its axis.
![Alt text](https://github.com/razainno/behavioral_cognitive/blob/master/home_work/exercise_6/3.gif "The robot gets stucked near the target")

> Run other experiments by using a feed-forward neural architecture (without memory). 
To enable Feed Forward neural network mode go to the ./xdiscrim folder and open ErDiscrim.ini file.
There find the line architecture:
``` bash
architecture = 3. Enables LSTM (Long Short Term Memory architecture)
architecture = 0. Enables Feed forward neural architecture without memory.
```
I've run experiments and noticed that sometimes the robot is able to reach the target, sometimes it moves very slowly and drives past the target, sometimes very quickly and can't reach. In all cases it can't stop near the target.
> Explain how the behavior of evolved robots differ from those evolved with the LSTM architecture (i.e. the Long Short Term Memory architecture).
I've run experiments and noticed that sometimes the robot is able to reach the target, sometimes it moves very slowly and drives past the target, sometimes very quickly and can't reach. In all cases it can't stop near the target. The robot doesn't know where to stop due to it hasn't feedback part and can't estimate the state properly. That is why it can go through the target and skip it


