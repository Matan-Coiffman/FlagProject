import pygame
import random

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.color.Color('dark green')
run = True

grass_image = pygame.image.load(r'bin/grass.png')
new_width, new_height = 50, 50  # Adjust the desired size here
grass_image = pygame.transform.scale(grass_image, (new_width, new_height))

grass_images = []

for i in range(20):
    x = random.randint(0, SCREEN_WIDTH - grass_image.get_width())
    y = random.randint(0, SCREEN_HEIGHT - grass_image.get_height())
    grass_images.append((x, y))

while run:
    screen.fill(background)
    for x, y in grass_images:
        screen.blit(grass_image, (x, y))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
