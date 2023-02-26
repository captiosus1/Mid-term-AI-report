class Agent:
    #constructor 
    def __init__(self, env, heuristic):
      #priority queue
        self.frontier = PriorityQueue()
          #explored list
        self.explored = dict()
        #start state
        self.startState = env.getStartState()
        self.goalState = env.getGoalState()
        #environment object
        self.env = env
        self.goalNode = None
        #heuristic function 
        self.heuristic = heuristic
    
    def start(self):
      #intializing the start node with no parent node
        initNode = Node(parent = None, state = self.startState, pcost = 0, hcost=0)
        #pushing the node in to frontier
        self.frontier.push(initNode)
        while not self.frontier.isEmpty():
          #popping the least cost function node
            currNode = self.frontier.pop()
            #getting all the child states of current state
            childStates = self.env.getChildStates(currNode.state)
            #storing the hash  of the current node into explored list 
            if hash(currNode) in self.explored:
                continue
            self.explored[hash(currNode)] = currNode
            #if we reach the goal state then terminate the loop
            if self.env.reachedGoal(currNode.state):
                self.goalNode = currNode
                break
            goalState = self.env.getGoalState()

            l = []
            #push all the nodes in to queue
            for state in childStates:
                  #calculating the hcost
                hcost = self.heuristic(state, goalState)
                #updating the node that is going to be pushed
                node = Node(parent=currNode, state=state, pcost=currNode.pcost+1, hcost=hcost)
                self.frontier.push(node)
        #returning the depth at which we reach goal state
        return self.depth()
    #calculating 
    def depth(self):
        node = self.goalNode
        depth = 0
        while node is not None:
            node.printState()
            node = node.parent
            depth+=1
        return depth


#defining different heustric
def heuristic0(currState, goalState):
    return 0


def misplaceTiles(currState, goalState):
    misplaces = 0
    for i in range(len(currState)):
        for j in range(len(currState[0])):
            if currState[i][j]!=goalState[i][j]:
                misplaces+=1
    return misplaces


def manhattan(currState, goalState):
    distance = 0
    for i in range(len(currState)):
        for j in range(len(currState[0])):
            val = currState[i][j]
            i_goal, j_goal = np.where(goalState==val)
            distance += abs(i_goal[0] - i) + abs(j_goal[0] - j)
    return distance