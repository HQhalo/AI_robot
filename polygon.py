from vertex import vertex
class polygon:
    def __init__(self,input):
        coordinates = input.split(',')
        self.vertices = []
        if len(coordinates) % 2 != 0 :
            print("invalue input")
        else :
            i = 0
            while i < len(coordinates):
                v = vertex(float(coordinates[i]),float(coordinates[i+1]))
                self.vertices.append(v)
                i = i+2
    def IsIntersection(self, vertex1,vertex2):

    def lineSegmentsIntersect(self,L1,L2,S1,S2):
        

