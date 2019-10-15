from point import *

class pointInfo:  
    def __init__(self,parent,g,h):
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h
        
