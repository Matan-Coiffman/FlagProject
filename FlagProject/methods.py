import pygame
import random


def move_player(player, matrix):
    y = 0
    x = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_direction = -1
            elif event.key == pygame.K_RIGHT:
                player_x_direction = 1
            elif event.key == pygame.K_UP:
                player_y_direction = -1
            elif event.key == pygame.K_DOWN:
                player_y_direction = 1


# def random_bushes(grass_images, grass_image, SCREEN_HEIGHT, SCREEN_WIDTH):
#     for i in range(20):
#         x = random.randint(0, SCREEN_WIDTH - grass_image.get_width())
#         y = random.randint(0, SCREEN_HEIGHT - grass_image.get_height())
#         grass_images.append((x, y))
