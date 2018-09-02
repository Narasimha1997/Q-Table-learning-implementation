import numpy
import random

class GameEnv : 

    def __init__(self):
        # Structure => state : [action : (reward, nextState) ...]
        self.state_table = {
            0 : [(-1000, -1), (10, 1), (-1000, -1), (0, 3), (0, 0)],
            1 : [(0, 0), (10, 2), (-1000, -1), (-100, 4), (0, 1)],
            2 : [(0, 1), (-1000, -1), (-1000, -1), (100, 5), (0, 2)],
            3 : [(-1000, -1), (-100, 4), (10, 0), (-1000, -1), (0, 3)],
            4 : [(0, 3), (0, 5), (0, 1), (-1000, -1), (-100, 4)],
            5 : [(-100, 4), (-1000, -1), (100, 2), (-1000, -1), (100, 5)]
        }

        self.actions = ["Left", "Right", "Up", "Down", "Same"]
        self.game_size = (6, 5)
    
    def getNextStateWithReward(self, state, action):
        return self.state_table[state][action]

    def play(self, Q, state):
        if state == 5 : return
        #choose optimal action having maximum Q value:
        action = numpy.argmax(Q[state])
        nextState = self.state_table[state][action][1]
        print("From state ", state, "Take ", self.actions[action], " to reach new state : ", nextState)
        self.play(Q, nextState)
        pass
        


''' Q table structure : 
    States -> rows (0 - 5)
    Actions -> (0 - 4) {left, right, up, down, nothing}
'''
Q = numpy.zeros((6, 5))

def learn(env, Q, gamma = 0.8, stateSize = 0, actionSize = 0):

    for i in range(10000):

        state = random.randint(a = 0, b = stateSize  -1)
        print('Start : ', state)

        while True :

            if state == 5 or state == -1 : break

            #make a random action:
            action = random.randint(a = 0, b = actionSize - 1)

            #get (reward, nextState from env):
            reward, nextState = env.getNextStateWithReward(state, action)
            if nextState == -1 or reward == -100: break

            #all rewards of next state:
            Q[state, action] = env.state_table[state][action][0] + gamma * numpy.argmax(Q[nextState])

            state = nextState

    return Q


env = GameEnv()
Q = learn(env, Q, stateSize = 6, actionSize = 5)
print(Q)

print("Started playing....")
env.play(Q, 0)