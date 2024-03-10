import pygame
pygame.init()
import math
import random

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Procedural")

x = 250
y = 250
r = 25
t = 25

run = True

while run:
    
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    mx, my = pygame.mouse.get_pos()
            
    screen.fill((0,0,0))
    cursor = pygame.draw.circle(screen, (0, 0, 0), (mx,my), r, t)
    c1 = pygame.draw.circle(screen, (0,255,0), (x,y), r, t)
    
    dx = mx - x
    dy = my - y
    
    angle = math.atan2(dx,dy)
    vx = math.sin(angle)
    vy = math.cos(angle)
    
    x += vx
    y+= vy
    
    pygame.display.update()
    
pygame.quit() 