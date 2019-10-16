import pygame
import sys
from config import *
from map import map 


def main():
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

    # cost,path = Map.UCS()
    # path = Map.AStar()
    # if path:
    #     for i in range(len(path)-1):
    #         pygame.draw.line(screen,GREEN,Map.mapPoint(path[i].toPixal()),Map.mapPoint(path[i+1].toPixal()),2)
    
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_d:
                            _,path = Map.DFS()
                            drawPath(path,screen,Map)
                        if event.key == pygame.K_b:
                            _,path = Map.BFS()
                            drawPath(path,screen,Map)
                        if event.key == pygame.K_u:
                            _,path = Map.UCS()
                            drawPath(path,screen,Map)
                        if event.key == pygame.K_a:
                            _,path = Map.AStar()
                            drawPath(path,screen,Map)


            pygame.display.flip()
            clock.tick(30)
def drawPath(path,screen,Map):
    if path:
        for i in range(len(path)-1):
            pygame.draw.line(screen,GREEN,Map.mapPoint(path[i].toPixal()),Map.mapPoint(path[i+1].toPixal()),2)

if __name__ == "__main__":
    main()