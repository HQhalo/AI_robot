import pygame
import sys
from point import *
from config import *
from map import map 


def main():
    Map = map(sys.argv[1])
    pygame.init()
    clock = pygame.time.Clock()

    done = False

    Map.draw()

    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True
                    if event.type == pygame.KEYDOWN:
                        Map.draw()
                        if event.key == pygame.K_d:
                            _,path = Map.DFS()
                        elif event.key == pygame.K_b:
                            _,path = Map.BFS()                          
                        elif event.key == pygame.K_u:
                            _,path = Map.UCS()                       
                        elif event.key == pygame.K_a:
                            _,path = Map.AStar()   
                        elif event.key == pygame.K_w:
                            Map.drawWaitPoint()
                            _,path = Map.collect_wait_point()
                            # _,path = Map.AStar()   

                        elif event.key == pygame.K_q:
                            done = True
                            break
                        else:
                            continue
                        if path:
                            Map.drawPath(path)
                            Map.drawCost(_)
                        else:
                            Map.drawText("khong co",point(Map.M+2,10),16)

            pygame.display.flip()
            clock.tick(30)

if __name__ == "__main__":
    main()