import pygame
import sys

pygame.init()

width,height = 800,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Animation")

blue=(30,144,255)
white=(255,255,255)

x,y = width//2,height//2
radius = 20
dx,dy=5,5

rect_x,rect_y=50,50
rect_width,rect_height = 100,50
rect_dx,rect_dy=7,3

running = True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
    # Circle
    x+=dx
    y+=dy
    if x-radius< 0 or x+radius>width:
        dx =-dx
    if y-radius< 0 or y+radius>height:
        dy =-dy
    # Rectangle
    rect_x +=rect_dx 
    rect_y +=rect_dy 
    if rect_x<0 or rect_x +rect_width>width:   
        rect_dx =-rect_dx
    if rect_y<0 or rect_y +rect_height>height:   
        rect_dy =-rect_dy
    window.fill(white)
    pygame.draw.circle(window,blue,(x,y),radius)
    pygame.draw.rect(window,blue,(rect_x,rect_y,rect_width,rect_height))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()