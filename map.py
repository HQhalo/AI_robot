from polygon import polygon
from point import point
from pointInfo import *
from config import *
import sys
import copy
import pygame

class map:

    def __init__(self ,input):
        

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
        self.wait_point = []

        n = int(lines[2])
        
        for i in range(n):
            p = polygon(lines[i+3])
            self.polygons.append(p)
            self.pointsMap = self.pointsMap + p.getPoints()
        
        if len(lines) > n-1+3:
            self.num_wait_point = int(lines[n+3])
            for i in range(self.num_wait_point):
                token_split = lines[n+3+i+1].split(',')
                tmp = point(float(token_split[0]),float(token_split[1]))
                self.pointsMap.append(tmp)
                self.wait_point.append(tmp)
        self.screen = pygame.display.set_mode(self.getSize())
        
    def getSize(self):
        return [(self.M+10)*RATIO, (self.N)*RATIO]
    def mapPoint(self,p):
        p[1] = self.getSize()[1]- p[1]
        return p 
    def mapListPoint(self,LP):
        for i in range(len(LP)):
            LP[i] = self.mapPoint(LP[i])
        return LP
    def outOfRect(self,p):
        return p.x<0 or p.x >self.M or p.y < 0 or p.y > self.N
    def generateChild(self,point1):
        children = []
        for i in self.pointsMap:
            if self.outOfRect(i):
                continue
            if i != point1:
                flag = False
                for j in self.polygons:
                    if j.IsIntersection(point1,i) == True:
                        flag = True
                        break
                if flag == False:
                    children.append(i)
        return children
    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen,WHITE,[0,0,self.M*RATIO, self.N*RATIO],5)

        for i in self.polygons:
            pygame.draw.polygon(self.screen, RED, self.mapListPoint(i.toListPixals()), 4)

        pygame.draw.circle(self.screen,RED,self.mapPoint(self.Start.toPixal()),10)
        pygame.draw.circle(self.screen,BLUE,self.mapPoint(self.Goal.toPixal()),10)

        self.drawText("Enter:",point(self.M+1,1),18)
        self.drawText("b : Run BFS",point(self.M+2,2),16)
        self.drawText("d : Run DFS",point(self.M+2,3),16)
        self.drawText("u : Run UCS",point(self.M+2,4),16)
        self.drawText("a : Run A star",point(self.M+2,5),16)
        self.drawText("w : Run collect waiting point",point(self.M+2,6),16)
        self.drawText("q : quit",point(self.M+2,8),16)
    def drawWaitPoint(self):
        for i in self.wait_point:
            pygame.draw.circle(self.screen,(255,153,18),self.mapPoint(i.toPixal()),10) 
    def drawText(self,text,coord,size):
        font = pygame.font.Font('freesansbold.ttf', size) 
        text = font.render(text, True, GREEN, BLUE) 
        textRect = text.get_rect()  
        textRect.midleft = (coord.x*RATIO, coord.y*RATIO) 
        self.screen.blit(text, textRect)

    def drawPath(self,path):
        if path:
            for i in range(len(path)-1):
                pygame.draw.line(self.screen,GREEN,self.mapPoint(path[i].toPixal()),self.mapPoint(path[i+1].toPixal()),2)
    def drawCost(self,cost):
        self.drawText("Cost: "+str(cost),point(self.M+1,self.N-1),16)
    def BFS(self):
        
        queue = []
        queue.append([self.Start])
        visited = dict()
        visited[self.Start] = 1
        while queue:
            path = queue.pop(0)
            node = path[-1]
                       
            if node == self.Goal:
                cost = 0
                for i in range(len(path)-1):
                    cost = cost + point.distance(path[i],path[i+1])
                return cost,path
            a = self.generateChild(node)
            for i in a: 
                if (i in visited) == False: # shit! dcm "( )"
                    newPath = path + [i]
                    visited[i]  = 1
                    queue.append(newPath)
        return 0,None
    def DFS(self):
        stack = []
        stack.append(self.Start)
        visited = dict()
        visited[self.Start] = 1
        while stack:
            flag = False
            node = stack[-1]
           
            if node == self.Goal:
                cost = 0
                for i in range(len(stack)-1):
                    cost = cost + point.distance(stack[i],stack[i+1])
                return cost,stack
            a = self.generateChild(node)
            for i in a: 
                if (i in visited) == False:
                    stack.append(i)
                    visited[i] = 1
                    flag = True
                    break                  
            if flag == False:
                stack.pop()
        return 0,None
        
    def UCS(self):
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
        return 0,None
        
    def AStar(self):
        OpenList = []
        CloseList = []
        pointInfos = dict()
        OpenList.append(self.Start)
        pointInfos[self.Start] = pointInfo(self.Start,0,0)

        while OpenList:
            node = OpenList[0]
            for i in OpenList:
                if pointInfos[i].f < pointInfos[node].f:
                    node = i
            OpenList.remove(node)

            if node == self.Goal:
                path =[]
                while node != self.Start:
                    path.insert(0,node)
                    node = pointInfos[node].parent
                path.insert(0,self.Start)
                cost = 0
                for i in range(len(path)-1):
                    cost = cost + point.distance(path[i],path[i+1])
                return cost,path
            
            CloseList.append(node)
            
            a = self.generateChild(node)
            for i in a:
                g = pointInfos[node].g+ point.distance(node,i)
                if (i in OpenList) == True:
                    if g < pointInfos[i].g:                      
                        pointInfos[i].g = g
                        pointInfos[i].parent = node
                        pointInfos[i].f = pointInfos[i].h + g
                elif (i in CloseList) == True:
                    if g < pointInfos[i].g:                     
                        pointInfos[i].g = g
                        pointInfos[i].parent = node
                        pointInfos[i].f = pointInfos[i].h + g
                    
                        stack = []
                        stack.append(i)
                        visited = dict()
                        visited[i] = 1
                        while stack:
                            flag = False
                            Tk_node = stack[-1]

                            par = pointInfos[Tk_node].parent
                            pointInfos[Tk_node].g = par.g + point.distance(par,pointInfos[Tk_node])

                            b = self.generateChild(Tk_node)
                            for i in b:
                                if (i in CloseList) == True or (i in OpenList) == True:
                                    if (i in visited) == False:
                                        stack.append(i)
                                        visited[i] = 1
                                        flag = True
                                        break
                            if flag == False:
                                stack.pop()   
                else:
                    OpenList.append(i)
                    pointInfos[i] = pointInfo(node,g,point.distance(i,self.Goal))
        return 0,None

    def collect_wait_pointHelper(self,start,goal):
        OpenList = []
        CloseList = []
        pointInfos = dict()
        OpenList.append(start)
        pointInfos[start] = pointInfo(start,0,0)

        while OpenList:
            node = OpenList[0]
            for i in OpenList:
                if pointInfos[i].f < pointInfos[node].f:
                    node = i
            OpenList.remove(node)

            if node == goal:
                path =[]
                while node != start:
                    path.insert(0,node)
                    node = pointInfos[node].parent
                path.insert(0,start)
                cost = 0
                for i in range(len(path)-1):
                    cost = cost + point.distance(path[i],path[i+1])
                return cost,path
            
            CloseList.append(node)
            
            a = self.generateChild(node)
            for i in a:
                g = pointInfos[node].g+ point.distance(node,i)
                if (i in OpenList) == True:
                    if g < pointInfos[i].g:                      
                        pointInfos[i].g = g
                        pointInfos[i].parent = node
                        pointInfos[i].f = pointInfos[i].h + g
                elif (i in CloseList) == True:
                    if g < pointInfos[i].g:                     
                        pointInfos[i].g = g
                        pointInfos[i].parent = node
                        pointInfos[i].f = pointInfos[i].h + g
                    
                        stack = []
                        stack.append(i)
                        visited = dict()
                        visited[i] = 1
                        while stack:
                            flag = False
                            Tk_node = stack[-1]

                            par = pointInfos[Tk_node].parent
                            pointInfos[Tk_node].g = par.g + point.distance(par,pointInfos[Tk_node])

                            b = self.generateChild(Tk_node)
                            for i in b:
                                if (i in CloseList) == True or (i in OpenList) == True:
                                    if (i in visited) == False:
                                        stack.append(i)
                                        visited[i] = 1
                                        flag = True
                           
                            if flag == False:
                                stack.pop()   
                else:
                    OpenList.append(i)
                    pointInfos[i] = pointInfo(node,g,point.distance(i,goal))
        return 0,None
    def collect_wait_point(self):
        
        start_point = self.Start
        visited = [0 for i in range(self.num_wait_point)]
        total_cost = 0
        total_path = []
        for k in range(self.num_wait_point):
            pos = -1
            min_dis = 0
            for i in range(self.num_wait_point):
                if visited[i] == 0:
                    if (point.distance(start_point, self.wait_point[i]) < min_dis) or (pos == -1):
                        min_dis = point.distance(start_point, self.wait_point[i])
                        pos = i
            print(pos)
            visited[pos] = 1
     
            cost,path = self.collect_wait_pointHelper(start_point,self.wait_point[pos])
            start_point = copy.deepcopy(self.wait_point[pos])
            
            total_cost = total_cost + cost
            total_path = total_path + path
     
        cost,path = self.collect_wait_pointHelper(start_point,self.Goal)   
        start_point = copy.deepcopy(self.wait_point[pos])

        total_cost = total_cost + cost
        total_path = total_path + path
    

        return total_cost, total_path