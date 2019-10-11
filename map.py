from polygon import polygon
from point import point
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
        visited = []
        for i in range(self.M):
            visited.append([ 0 for i in range(self.N)])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            # print(path)
            visited[int(node.x)][int(node.y)] = 1
            if node == self.Goal:
               return path
            a = self.generateChild(node)
            for i in a:
                if visited[int(i.x)][int(i.y)] == 0:
                    newPath = path + [i]
                    visited[int(i.x)][int(i.y)]  = 1
                    queue.append(newPath)
if __name__ == "__main__":
    Map = map(sys.argv[1])
    # Map.printM()
    # p1 = point(float(sys.argv[1]),float(sys.argv[2]))
    # p2 = point(float(sys.argv[3]),float(sys.argv[4]))
    # p3 = point(float(sys.argv[5]),float(sys.argv[6]))
    # p4 = point(float(sys.argv[7]),float(sys.argv[8]))
    # po = polygon("4,4,6,1,2,2,2,4")
    # print(po.lineSegmentsIntersect(p1,p2,p3,p4))
    # print(po.IsIntersection(p1,p2))
    a =Map.BFS()
   
