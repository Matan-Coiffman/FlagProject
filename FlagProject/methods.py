import pygame
import random


def move_player_matrix(current_pos):
    x, y = current_pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = max(0, x - 1)
    if keys[pygame.K_RIGHT]:
        x = min(49, x + 1)
    if keys[pygame.K_UP]:
        y = max(0, y - 1)
    if keys[pygame.K_DOWN]:
        y = min(19, y + 1)
    return [x, y]


def place_ts(matrix, placed_mines):
    for i in range(20):
        placed = False
        while not placed:
            row = random.randint(6, len(matrix) - 1)
            start_col = random.randint(0, len(matrix[0]) - 3)

            if matrix[row][start_col] == "0" and matrix[row][
                start_col + 1] == "0" and matrix[row][start_col + 2] == "0":
                matrix[row][start_col] = "T"
                matrix[row][start_col + 1] = "T"
                matrix[row][start_col + 2] = "T"
                placed = True
        x = start_col + 1
        y = row
        placed_mines.append([x, y])
    return placed_mines


def is_bombed(current_pos, placed_mines):
    legs_positions = [
        [current_pos[0], current_pos[1] + 5],
        [current_pos[0] + 1, current_pos[1] + 5]
    ]

    for mine in placed_mines:
        for leg in legs_positions:
            if leg[0] == mine[0] and leg[1] == mine[1] or leg[0] == mine[0] + 1 and leg[1] == mine[1] or leg[0] == mine[0] - 1 and leg[1] == mine[1]:
                return True
    return False


def check_victory(player_pos, flag_pos, cell_width_jump, cell_height_jump):
    body_positions = [
        [player_pos[0], player_pos[1] + i] for i in range(6)
    ]

    flag_x_range = range(flag_pos[0] // cell_width_jump, (
            flag_pos[0] + 3 * cell_width_jump) // cell_width_jump)
    flag_y_range = range(flag_pos[1] // cell_height_jump, (
            flag_pos[1] + 3 * cell_height_jump) // cell_height_jump)

    for body_part in body_positions:
        if body_part[0] in flag_x_range and body_part[1] in flag_y_range:
            return True
    return False
