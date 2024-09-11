import pygame
import random
import methods
import copy

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.color.Color('dark green')
grid_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid_background = pygame.color.Color('black')

font = pygame.font.SysFont(None, 55)

run = True
game_over = False
message = ""
cell_width_jump = SCREEN_WIDTH // 50
cell_height_jump = SCREEN_HEIGHT // 25
grass_image = pygame.image.load(r'bin/grass.png')
mine_image = pygame.image.load(r'bin/mine.png')
soldier_image = pygame.image.load(
        r'bin/soldier.png')
flag_image = pygame.image.load(r'bin/flag.png')

matrix = []
placed_mines = []
grass_images = []


grass_image = pygame.transform.scale(grass_image, (50, 50))
mine_image = pygame.transform.scale(mine_image,
                                    (cell_width_jump * 3, cell_height_jump))
soldier_image = pygame.transform.scale(soldier_image, (
    cell_width_jump * 5, cell_height_jump * 6))
flag_image = pygame.transform.scale(flag_image, (
    cell_width_jump * 3, cell_height_jump * 3))


for row in range(25):
    matrix_row = []
    for col in range(50):
        matrix_row.append("0")
    matrix.append(matrix_row)

placed_mines = methods.place_ts(matrix, placed_mines)
placed_mines_Index = copy.deepcopy(
        placed_mines)

# Grass placement
for i in range(20):
    x = random.randint(0, SCREEN_WIDTH - grass_image.get_width())
    y = random.randint(0, SCREEN_HEIGHT - grass_image.get_height())
    grass_images.append((x, y))

for i in placed_mines:
    i[0] = i[0] * cell_width_jump
    i[1] = i[1] * cell_height_jump

player_pos = [0, 0]
flag_pos = [SCREEN_WIDTH - cell_width_jump * 3,
            SCREEN_HEIGHT - cell_height_jump * 4]


def switch_screen(screen_to_display, player_pos):
    screen_to_display.fill(grid_background)
    for x, y in placed_mines:
        screen.blit(mine_image, (x - cell_width_jump, y))
    for row in range(25):
        for col in range(50):
            pygame.draw.rect(screen_to_display,
                             pygame.color.Color('dark green'), (
                                 col * cell_width_jump, row * cell_height_jump,
                                 cell_width_jump, cell_height_jump), 1)
    screen.blit(soldier_image, (
        player_pos[0] * cell_width_jump, player_pos[1] * cell_height_jump))
    pygame.display.flip()


def display_message(message):
    text = font.render(message, True, (255, 0, 0))  # Red color for visibility
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                       SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()


clock = pygame.time.Clock()
while run:
    screen.fill(background)

    for x, y in grass_images:
        screen.blit(grass_image, (x, y))
    screen.blit(flag_image, (flag_pos[0], flag_pos[1]))

    screen.blit(soldier_image, (
        player_pos[0] * cell_width_jump, player_pos[1] * cell_height_jump))

    if game_over:
        display_message(message)
        pygame.time.delay(3000)
        run = False
    else:
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            switch_screen(grid_screen, player_pos)
            pygame.time.delay(1000)

    if not game_over:
        player_pos = methods.move_player_matrix(player_pos)

        if methods.is_bombed(player_pos, placed_mines_Index):
            message = "Game Over!"
            game_over = True

        if methods.check_victory(player_pos, flag_pos, cell_width_jump,
                                 cell_height_jump):
            message = "You won! Reached the flag."
            game_over = True

    clock.tick(10)

pygame.quit()
