import pygame
import sys
import random

pygame.init()

VEL = 15  # Reduced velocity for slower movement
t = 15
FPS = 9  # Reduced FPS for slower movement

COL = (255, 255, 255)

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

head = [250, 250]  # pos x and y
body = [[240, 250], [230, 250], [220, 250], [210, 250]]


def move():
    global head, body

    # Generate random direction for the head's movement
    direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    # Update head position based on random direction and velocity
    head[0] += VEL * direction[0]
    head[1] += VEL * direction[1]

    # Wrap around the screen if head goes out of bounds
    head[0] %= 500
    head[1] %= 500

    body.insert(0, list(head))
    del body[-1]


def draw(screen):
    for segment in body:
        pygame.draw.circle(screen, COL, segment, t)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    move()
    screen.fill((0, 0, 0))
    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
