import numpy as np
#environment class
# question 2
class Environment():
    #constructor
    def __init__(self, depth = None, goalState = None):
        self.goalState = goalState
        self.depth = depth
        self.startState = self.generateStartState()
    #generating a start state from the randomly
    def generateStartState(self):
        tempState = np.array([1, 2, 3, 4, 5, 6, 7, 8, '_'])
        np.random.shuffle(tempState)
        tempState = tempState.reshape(3,3)
        return tempState.tolist()
    
    #returns the satrt state
    def getStartState(self):
        return self.startState
    #returns the goal state
    def getGoalState(self):
        return self.goalState
    #returns the child states
    def getChildStates(self, state):
        rowCol = (0,0)
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] == '_':
                    rowCol = (i,j)
                    break
        #lsit consisting of all the chidren states
        childStates = []
        #rowCol indication the row and column of the blank 
        if rowCol[0] > 0: #it can move up as the zero is not in first row
          #deepcopy of current state into temp child state
            childState = np.copy(state)
            
            #swaping the numbers using temp variable
            val = childState[rowCol[0], rowCol[1]]
            childState[rowCol[0], rowCol[1]]  = childState[rowCol[0]-1, rowCol[1]]
            childState[rowCol[0]-1, rowCol[1]] = val
            #adding the current state into list of childrensattes
            childStates.append(childState)
            #here the blank can go down as the blank is not in last row 
        if rowCol[0] < 2:
            childState = np.copy(state)
            # swapping the blank with the number
            val = childState[rowCol[0], rowCol[1]]
            #swapping the tile with temp variable
            childState[rowCol[0], rowCol[1]]  = childState[rowCol[0]+1, rowCol[1]]
            childState[rowCol[0]+1, rowCol[1]] = val
            #adding the state to the list
            childStates.append(childState)
        #here the blank can go right as the blank is not in last column
        if rowCol[1]<2:
            childState = np.copy(state)
            #swapping the tile using temp variable
            val = childState[rowCol[0], rowCol[1]]
            childState[rowCol[0], rowCol[1]] = childState[rowCol[0], rowCol[1]+1]
            childState[rowCol[0], rowCol[1]+1] = val
            #adding the state into list 
            childStates.append(childState)
            
        if rowCol[1] > 0:
          #here the blank can go left as the blank is not in first column
            childState = np.copy(state)
            #swap the blank
            val = childState[rowCol[0], rowCol[1]]
            childState[rowCol[0], rowCol[1]] = childState[rowCol[0], rowCol[1]-1]
            childState[rowCol[0], rowCol[1]-1] = val
            #add it to the list
            childStates.append(childState)
        #return the list containing all the nextStates to the agent
        return childStates
    #function to check if we reached the goal state or not
    def reachedGoal(self, state):
        for i in range(len(state)):
            for j in range(len(state[0])):
                if state[i][j] != self.goalState[i][j]:
                    return False
        return True