import pygame
import sys
from config import *
from map import map 


if __name__ == "__main__":
    Map = map(sys.argv[1])
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(Map.getSize())
    
    done = False
    pygame.draw.rect(screen,WHITE,[0,0,Map.M*RATIO, Map.N*RATIO],5)

    for i in Map.polygons:
        pygame.draw.polygon(screen, RED, Map.mapListPoint(i.toListPixals()), 5)

    pygame.draw.circle(screen,RED,Map.mapPoint(Map.Start.toPixal()),10)
    pygame.draw.circle(screen,BLUE,Map.mapPoint(Map.Goal.toPixal()),10)

    cost,path = Map.UCS()
    # path = Map.BFS()
    if path:
        for i in range(len(path)-1):
            pygame.draw.line(screen,GREEN,Map.mapPoint(path[i].toPixal()),Map.mapPoint(path[i+1].toPixal()),2)
    
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True           
            pygame.display.flip()
            clock.tick(30)