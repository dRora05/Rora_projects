import pygame
import sys
import math
pygame.init()

VEL = 20
t = 15
FPS = 10

COL = (255, 255, 255)

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

head = [250, 250] # pos x and y
body = [[240, 250], [230, 250], [220, 250], [210, 250]]

def move():
    global head, body
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        head[0] += VEL 
    if keys[pygame.K_LEFT]:
        head[0] -= VEL 
    if keys[pygame.K_UP]:
        head[1] -= VEL 
    if keys[pygame.K_DOWN]:
        head[1] += VEL 

    body.insert(0, list(head))
    del body[-1]

def draw(screen):
    for segment in body:
        c1 = pygame.draw.circle(screen, COL, segment, t)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move()
    screen.fill((0,0,0))
    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
