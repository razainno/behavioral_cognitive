# Exercise 5: 
## Implementation to create  a new Gym/Bullet environment 
* i have followed this tutorial to creaate the environment for balancebot_robot
> https://backyardrobotics.eu/2017/11/27/build-a-balancing-bot-with-openai-gym-pt-i-setting-up/. 

. I used OpenAI Gym, Baselines and pyBullet to implement this task. As the result I've created new environment 'balancebot.v0'. It has  xml-file with robot description  and structure , "balancebot_env.py" script, which contains main environment methods (init(), seed(), step(), reset(), render(), methods to estimate the reaward,observations, actuators and termination processs) and all neccesary files.
 
1. Build the environment:
``` bash
cd balance-bot
pip install -e .
```
2.created environment is used by:
```
import balance_bot

3. To chek the enivornment i have run this command to see the result
```
python3 balancebot_task.py

The following output is obtained
Here you can see the screenshot from the simulation
![Alt text](https://github.com/rodosha98/Behavioural-and-Cognitive-Robotics/blob/task4-6/Exercise5/balancebot.jpg "The balancebot simulation in the new environment.")
