from polygon import polygon
from vertex import vertex
import sys
class map:
    def __init__(self , input):
        f = open(input,"r")
        lines = f.readlines()
        
        temp = lines[0].split(',')
        self.M = float(temp[0])
        self.N = float(temp[1])

        temp =lines[1].split(',')
        self.Start = vertex(float(temp[0]),float(temp[1]))
        self.Goal = vertex(float(temp[2]),float(temp[3]))

        n = int(lines[2])
        self.polygons = []
        for i in range(n):
            p = polygon(lines[i+3])
            self.polygons.append(p)
    def printM(self):
        print(str(self.M) +str(self.N))

if __name__ == "__main__":
    Map = map(sys.argv[1])
    Map.printM()