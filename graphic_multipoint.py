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
    for i in Map.wait_point:
        pygame.draw.circle(screen,(255,153,18),Map.mapPoint(i.toPixal()),10)

    Map.draw()

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                search_kind = None
                if event.type == pygame.KEYDOWN:

                    Map.draw()

                    if event.key == pygame.K_d:
                        search_kind =  map.DFS
                        
                    if event.key == pygame.K_b:
                        search_kind =  map.BFS
                        
                    if event.key == pygame.K_u:
                        search_kind =  map.UCS
                        
                    if event.key == pygame.K_a:
                        search_kind =  map.AStar
                    
                    if event.key == pygame.K_q:
                        done = True
                        break

                    if search_kind != None:
                        
                        cost,path = Map.collect_wait_point(search_kind)
                        Map.drawCost(cost)
                        Map.drawPath(path)
                        
        pygame.display.flip()
        clock.tick(30)
            
    