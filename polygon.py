from point import point
from config import *
class polygon:

    def __init__(self,input):
        coordinates = input.split(',')
        self.vertices = []
        if len(coordinates) % 2 != 0 :
            print("invalue input")
        else :
            i = 0
            while i < len(coordinates):
                v = point(float(coordinates[i]),float(coordinates[i+1]))
                self.vertices.append(v)
                i = i+2
    def toList(self):
        re = []
        for i in self.vertices:
            re.append([int(i.x*RATIO),int(i.y*RATIO)])
        return re
    def getPoints(self):
        return self.vertices

    def IsIntersection(self, point1,point2):
        for i  in range(len(self.vertices)):
            if self.lineSegmentsIntersect(point1,point2,self.vertices[i-1],self.vertices[i]) == True:
               return True
        return False 

    def cross_product(self,p1, p2):
	    return p1.x * p2.y - p2.x * p1.y
    
    def direction(self,p1, p2, p3):
	    return  self.cross_product(p3.subtract(p1), p2.subtract(p1))

    def on_segment(self,p1, p2, p):
        return min(p1.x, p2.x) <= p.x <= max(p1.x, p2.x) and min(p1.y, p2.y) <= p.y <= max(p1.y, p2.y)   
    
    def lineSegmentsIntersect(self,p1, p2, p3, p4):
        if p1 == p3 or p1 == p4 or p2 == p3 or p2 ==p4:
            return False
        d1 = self.direction(p3, p4, p1)
        d2 = self.direction(p3, p4, p2)
        d3 = self.direction(p1, p2, p3)
        d4 = self.direction(p1, p2, p4)

        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
            ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True

        elif d1 == 0 and self.on_segment(p3, p4, p1):
            return True
        elif d2 == 0 and self.on_segment(p3, p4, p2):
            return True
        elif d3 == 0 and self.on_segment(p1, p2, p3):
            return True
        elif d4 == 0 and self.on_segment(p1, p2, p4):
            return True
        else:
            return False

