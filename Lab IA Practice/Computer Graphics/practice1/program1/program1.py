import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 800,600
WHITE=(255,255,255)
BLACK=(0,0,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Program 1 By Anish Kumar")

def draw_line_algorithm(x0,y0,x1,y1):
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    
    steep = dy > dx
    
    if steep:
        x0,y0=y0,x0
        x1,y1=y1,x1
    
    swapped = False
    if x0>x1:
        x0,x1=x1,x0
        y0,y1=y1,y0
        swapped=True
        
    dx = x1-x0
    dy = y1-y0
    
    error = int(dx/2.0)
    ystep = 1 if y0 < y1 else -1
    
    y = y0
    points = []
    for x in range(x0,x1+1):
        coord = (y,x) if steep else (x,y)
        points.append(coord)
        error -=abs(dy)
        if error <0:
            y+=ystep
            error +=dx
    if swapped:
        points.reverse()
    return points

def main():
    start_points1 = (0,0)
    end_points1=(800,600)
    start_points2 = (800,0)
    end_points2=(0,600)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(WHITE)
        
        line_points = draw_line_algorithm(*start_points1,*end_points1)
        line_points1 = draw_line_algorithm(*start_points2,*end_points2)
        for point in line_points:
            pygame.draw.circle(screen,BLACK,point,1)
        for point in line_points1:
            pygame.draw.circle(screen,BLACK,point,1)
        pygame.display.flip()
    pygame.quit()
    
if __name__=="__main__":
    main()
            