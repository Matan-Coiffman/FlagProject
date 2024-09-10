import pygame
import time

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.color.Color('dark green')
run = True
# Calculate cell size
cell_width_jump = SCREEN_WIDTH // 50
cell_height_jump = SCREEN_HEIGHT // 25

width_count = 0
height_count = 0
matrix = []

for row in range(SCREEN_HEIGHT // cell_height_jump):
    matrix_row = []
    for col in range(SCREEN_WIDTH // cell_width_jump):
        matrix_row.append("0")
    matrix.append(matrix_row)

while run:
    screen.fill(background)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
