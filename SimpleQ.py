import numpy
import random

state_table = numpy.array([
    [0, 0, 0, -1, -1,],
    [-1, 0, 0, 0, 100],
    [-1, -1 ,0, 0, -1],
    [0, -1, -1, 0, 100],
    [-1, -1, -1, -1, 100]
 ])

Q = numpy.zeros((5, 5))


def learn(Q, gamma = 0.80) :

    for i in range(1000):
        state = random.randint(0, 3)
        current_state = state
        print('Start : ', state)
        while True:
            rewards = state_table[state]
            action = random.randint(0, len(rewards) - 1)    
            if rewards[action] == -1 : continue
            next_state = action      
                #implement bellman equation to update Q value : 
            Q[state, next_state] = state_table[state , next_state] + gamma * max(Q[next_state])
            print(Q, end = '\n\n')
            state = next_state
            rewards = state_table[next_state] 
            if next_state == len(state_table) - 1 :break
        print('\n')
    return Q


def play(state, action, Q) :

    #we obtain max value from Q table from that state as action
    print("State : ", state, "Reward : ", Q[state][action])
    new_state  , new_action = action, numpy.argmax(Q[action])
    #print(new_action, new_state)
    if state == 4 : 
        return 
    return play(new_state, new_action,  Q)


Q = learn(Q)
play(0, 0 ,Q)