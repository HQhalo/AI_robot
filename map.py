from polygon import polygon
from point import point
from config import *
import sys
class map:

    def __init__(self , input):
        f = open(input,"r")
        lines = f.readlines()
        
        temp = lines[0].split(',')
        self.M = int(temp[0])
        self.N = int(temp[1])

        temp =lines[1].split(',')
        
        self.Start = point(float(temp[0]),float(temp[1]))
        self.Goal = point(float(temp[2]),float(temp[3]))
        
        self.polygons = []
        self.pointsMap = []
        self.pointsMap.append(self.Start)
        self.pointsMap.append(self.Goal)

        n = int(lines[2])
        
        for i in range(n):
            p = polygon(lines[i+3])
            self.polygons.append(p)
            self.pointsMap = self.pointsMap + p.getPoints()
    def getSize(self):
        return [self.M*RATIO, self.N*RATIO]
    def mapPoint(self,p):
        p[1] = self.getSize()[1]- p[1]
        return p 
    def mapListPoint(self,LP):
        for i in range(len(LP)):
            LP[i] = self.mapPoint(LP[i])
        return LP
    def generateChild(self,point1):
        children = []
        for i in self.pointsMap:
            if i != point1:
                flag = False
                for j in self.polygons:
                    if j.IsIntersection(point1,i) == True:
                        flag = True
                        break
                if flag == False:
                    children.append(i)
        return children
    def BFS(self):
        
        queue = []
        queue.append([self.Start])
        visited = dict()
        visited[self.Start] = 1
        while queue:
            path = queue.pop(0)
            node = path[-1]
                       
            if node == self.Goal:    
                return path
            a = self.generateChild(node)
            for i in a: 
                if (i in visited) == False: # shit! dcm "( )"
                    newPath = path + [i]
                    visited[i]  = 1
                    queue.append(newPath)
    def DFS(self):
        stack = []
        stack.append(self.Start)
        visited = dict()
        visited[self.Start] = 1
        while stack:
            flag = False
            node = stack[-1]
           
            if node == self.Goal:
                return stack
            a = self.generateChild(node)
            for i in a: 
                if (i in visited) == False:
                    stack.append(i)
                    visited[i] = 1
                    flag = True
                    break
            if flag == False:
                stack.pop()
    def UCS_(self):
        pQueue = []
        pQueueCost = []
        tracingQueue = []
        visited = dict()
        
        pQueue.append(self.Start)
        tracingQueue.append([self.Start])
        pQueueCost.append(0)
        while pQueue:         
            m= min(pQueueCost)
            idx = pQueueCost.index(m)
            cost = pQueueCost.pop(idx)
            node = pQueue.pop(idx)
            path = tracingQueue.pop(idx)
            visited[node] = False

            if node == self.Goal:
               return [cost,path]
            a = self.generateChild(node)

            for i in a: 
                costNew = cost + point.distance(node,i) 
                newPath = path + [i]
                if (i in pQueue) and costNew < pQueueCost[pQueue.index(i)]:
                    idx = pQueue.index(i)
                    pQueueCost[idx] = costNew
                    tracingQueue[idx] = newPath
                else:
                    if (i in visited) == False:
                        pQueue.append(i)
                        pQueueCost.append(costNew)
                        tracingQueue.append(newPath)
    def UCS(self):
        
    def AStar(self):
        return 0   