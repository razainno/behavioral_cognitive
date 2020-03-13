import gym
env = gym.make('CartPole-v0')
env.reset()
import numpy as np
pvariance = 0.1
        # variance of initial parameters
ppvariance = 0.02
        # variance of perturbations
nhiddens = 5
parameter = np.random.randn(20,37)*pvariance
rewar_list=[];
#print(parameter)
addition = lambda x:x + ppvariance       
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n
    #print(noutputs)

for i in range(20):
    r=0;
    W1 = (parameter[i][0:20]) 
    W1=W1.reshape(5,4)*pvariance
    W2 = (parameter[i][20:30]) 
    W2=W2.reshape(2,5)*pvariance
    b1 = (parameter[i][30:35])
    b1=b1.reshape(5,1)
    b2 = (parameter[i,35:37])
    b2=b2.reshape(2,1)
    observation = env.reset()
 
    for t in range(200):
        
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(W1, observation) + b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(W2, A1) + b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if actions are discrete we select the action corresponding to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):

            action = A2
        else:
            action = np.argmax(A2)
        env.render()
        observation, reward, done, info = env.step(action)
        #print(observation)
        if reward==1:

            r=r+1
    env.close()        
    reward=r 
    print("reward for this episode",reward)
    rewar_list.append(r)
list1= np.argsort(rewar_list)
print(list1)
#print(list1[0])
rewar_list=[]

for c,d in zip(range(0, 10), range(10, 20)):
    parameter[list1[c]]=addition(parameter[list1[d]])

for trial in range (0,5):
    for c in range (0,30):
        r = 0
        rewar_list = []

        for i in range(20):
            r=0;
            W1 = (parameter[i][0:20]) 
            W1=W1.reshape(5,4) 
            W2 = (parameter[i][20:30]) 
            W2=W2.reshape(2,5) 
            b1 = (parameter[i][30:35])
            b1=b1.reshape(5,1)
            b2 = (parameter[i][35:37])
            b2=b2.reshape(2,1)
            observation = env.reset()

            for t in range(200):
                # convert the observation array into a matrix with 1 column and ninputs rows
                observation.resize(ninputs,1)
                # compute the netinput of the first layer of neurons
                Z1 = np.dot(W1, observation) + b1
                # compute the activation of the first layer of neurons with the tanh function
                A1 = np.tanh(Z1)
                # compute the netinput of the second layer of neurons
                Z2 = np.dot(W2, A1) + b2
                # compute the activation of the second layer of neurons with the tanh function
                A2 = np.tanh(Z2)
                # if actions are discrete we select the action corresponding to the most activated unit
                if (isinstance(env.action_space, gym.spaces.box.Box)):

                    action = A2
                else:
                    action = np.argmax(A2)
                env.render()
                observation, reward, done, info = env.step(action)
                #print(observation)
                if reward==1:

                    r+=1
                
                    
                env.close() 
            reward=r
            print("reward for this episode "+str(i)+" and iteration "+str(c),reward)
            rewar_list.append(r)
            r=0
        list1= np.argsort(rewar_list)
        print(list1)
        #print(list1[0])
        for c,d in zip(range(0, 10), range(10, 20)):
            parameter[list1[c]]=addition(parameter[list1[d]])

np.savetxt('parameter_matrix.csv', parameter_matrix, delimiter=',')
np.save('test_Cartpole.npy',parameter_matrix)


