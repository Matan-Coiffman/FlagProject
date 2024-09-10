import pygame


def move_player(player, screenSize):
    player_x_direction = 0
    player_y_direction = 0
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

    player.x += player_x_direction * player.speed
    player.y += player_y_direction * player.speed

    player.x = max(0, min(player.x, screenSize[0] - player.width))
    player.y = max(0, min(player.y, screenSize[1] - player.height))
