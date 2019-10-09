import math
class vertex:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(self, vertex1, vertex2):
        return math.sqrt(math.pow(vertex1.x - vertex2.x)+math.pow(vertex1.y-vertex2.y))