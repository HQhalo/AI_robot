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
                        # path = Map.BFS()
                        Map.drawCost(cost)
                        Map.drawPath(path)

        pygame.display.flip()
        clock.tick(30)
            
    