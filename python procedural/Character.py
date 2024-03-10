import pygame
import sys
import math

pygame.init()

VEL = 20  # Velocity
t = 15  # Size of the segments
FPS = 10  # Frames per second
COL = (255, 255, 255)  # Color of the segments

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

head = [250, 250]  # Head position [x, y]
body = [[240, 250], [230, 250], [220, 250], [210, 250]]  # Body positions

follow_cursor = False  # Flag to toggle following cursor

# Load background image
background = pygame.image.load("bg.png").convert()

def move():
    global head, body, follow_cursor
    if follow_cursor:
        mouse_pos = pygame.mouse.get_pos()
        angle = math.atan2(mouse_pos[1] - head[1], mouse_pos[0] - head[0])
        head[0] += VEL * math.cos(angle)
        head[1] += VEL * math.sin(angle)
        body.insert(0, list(head))
        del body[-1]


def draw(screen):
    # Blit background image
    screen.blit(background, (0, 0))
    for segment in body:
        pygame.draw.circle(screen, COL, segment, t)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            follow_cursor = not follow_cursor  # Toggle follow cursor

    move()
    screen.fill((0, 0, 0))  # Fill the screen with black (optional)
    draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
