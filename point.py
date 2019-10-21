import math
from config import *

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def subtract(self, p):
    	return point(self.x - p.x, self.y - p.y)

    def __eq__(self,other):
        return abs(self.x - other.x) < 0.2 and abs(self.y - other.y)<0.2
    def __ne__(self,other):
        return abs(self.x - other.x) >= 0.2 or abs(self.y - other.y)>=0.2
        

    def __ne__(self,other):
        return self.x != other.x or self.y != other.y
    def toPixal(self):
        return [int(self.x*RATIO),int(self.y*RATIO)]
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __hash__(self):
        return hash(self.__str__())
    def __add__(self,other):
        return point(self.x+other.x,self.y+other.y)
    @staticmethod
    def distance(point1, point2):
        return math.sqrt(math.pow(point1.x - point2.x,2)+math.pow(point1.y-point2.y,2))