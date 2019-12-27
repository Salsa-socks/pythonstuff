#!usr/bin/env python

from queue import PriorityQueue

class State(object):
    def __init__(self, value, parent, start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
            
    def getDist(self):
        pass
    
    def createChildren(self):
        pass
    
class State_Spring(State):
    def __init__(self, value, parent, start =  0, goal = 0):
        super(State_Spring, self).__init__(value, parent, start, goal)
        self.dist = self.getDist()
        
    def getDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            try:
                dist += abs(i - self.value.index(letter))
            except:
                dist += abs(i - self.value.find(letter))
        return dist
    
    def createChildren(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = State_Spring(val, self)
                self.children.append(child)
                
class Astar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visitedQ = []
        self.priorityQ = PriorityQueue()
        self.start = start
        self.goal = goal
        
    def Solve(self):
        startState = State_Spring(self.start, 0, self.start, self.goal)
        count = 0
        self.priorityQ.put((0, count, startState))
        while not self.path and self.priorityQ.qsize():
            closestChild = self.priorityQ.get()[2]
            closestChild.createChildren()
            self.visitedQ.append(closestChild.value)
            for child in closestChild.children:
                if child.value not in self.visitedQ:
                    count += 1
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priorityQ.put((child.dist, count, child))
        if not self.path:
            print("Goal of " + self.goal + " is not possible")
        return self.path
    
# main

if __name__ == '__main__':
    start1 = "qazwsxedcrfvtgbyhnujmikolp"
    goal1 = "abcdefghijklmnopqrstuvwxyz"
    print("starting...")
    a = Astar_Solver(start1, goal1)
    a.Solve()
    for i in range(len(a.path)):
        print("{0}) {1}".format(i, a.path[i]))