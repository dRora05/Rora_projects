import pygame
import math

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Procedural")

bullet_x = 250  # Initial bullet position
bullet_y = 250
bullet_radius = 5  # bullet radius
bullet_thickness = 5  # bullet thickness

cursor_radius = 5  # cursor radius
cursor_thickness = 5  # cursor thickness

bullet_color = (255, 255, 255)
cursor_color = (0, 0, 0)
velocity = 5  # Velocity of the bullet

run = True
clicked_position = None  # Store initial position of cursor when mouse button is clicked

while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
            clicked_position = pygame.mouse.get_pos()  # Store initial position of cursor
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Check left mouse button release
            if clicked_position is not None:
                bullet_x, bullet_y = clicked_position  # Move bullet to clicked position
                clicked_position = None  # Reset clicked position

    mx, my = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))
    cursor = pygame.draw.circle(screen, cursor_color, (mx, my), cursor_radius, cursor_thickness)
    bullet = pygame.draw.circle(screen, bullet_color, (int(bullet_x), int(bullet_y)), bullet_radius, bullet_thickness)
    pygame.display.update()

pygame.quit()
