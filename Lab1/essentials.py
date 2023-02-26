import numpy as np
class Node:#struct consisting of all information about states and others
    def __init__(self, parent, state, pcost, hcost):
        
        self.parent = parent #parent state
        self.state = state
        self.pcost = pcost
        #heustric cost
        self.hcost = hcost
        #total cost
        self.cost = pcost + hcost
    def printState(self):
        print(self.state)
#fronteir to store the next states
class PriorityQueue():
    #constructor
    def __init__(self):
        self.q = []
        
    def push(self, node):
      #pushing the node into queue
        self.q.append(node)
    #pop function popping out node with least total cost
    def pop(self):
        #random state
        newState = None
        totalCost = 100000000000
        ind = -1
        #updating cost 
        for i in range(len(self.q)):
            
            if self.q[i].cost<totalCost:
                totalCost = self.q[i].cost
                ind = i
        
        return self.q.pop(ind)
    #checking whether the fronteir is empty or not
    #if empty then return false not reachable
    def isEmpty(self):      
        if len(self.q)==0:
            return True
        else:
            return False   
