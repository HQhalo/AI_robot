import pygame
import sys
from config import *
from map import map 



if __name__ == "__main__":
    Map = map(sys.argv[1])
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((Map.M*RATIO, Map.N*RATIO))
    
    done = False
    pygame.draw.rect(screen,WHITE,[0,0,Map.M*RATIO, Map.N*RATIO],5)

    for i in Map.polygons:
        pygame.draw.polygon(screen, RED, i.toList(), 2)

    pygame.draw.circle(screen,RED,Map.Start.toList(),10)
    pygame.draw.circle(screen,RED,Map.Goal.toList(),10)

    path = Map.BFS()
    if path:
        for i in range(len(path)-1):
            pygame.draw.line(screen,GREEN,path[i].toList(),path[i+1].toList(),3)
    
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True           
            pygame.display.flip()
            clock.tick(30)