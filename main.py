import pygame
import sys
import numpy as np
pygame.init()

# nariše črte za križec krožec
def draw_lines():
    # horizontal line 1
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # horizontal line 2
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # vertical line 1
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # vertical line 2
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# označi kvadrat
def mark_square(row, col, player):
    board[row] [col] = player

# ali je kvadrat prost
def avaible_square(row, col):
    if board [row][col] == 0:
        return True
    else:
        return False
    
# ali so vsa mesta zapolnjena
def is_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board [row] [col] == 0:
                return False
            
    return True

# nariši X/O v kvadrat v katerega pritisneš
def draw_XO():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):

            # player 1 turn
            if board[row] [col] == 1:
                pygame.draw.circle(screen, O_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)

            # player 2 turn
            elif board[row] [col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), X_WIDTH)

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 7
X_WIDTH = 25
SPACE = 50
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3

# colors
LINE_COLOR = (0, 0, 0)
BG_COLOR = (0, 255, 255)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))  
title = pygame.display.set_caption("Tic Tac Toe") 
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

player = 1

draw_lines()
#draw_XO()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]


            # izračuna pozicijo kvadratkov v [0] [1] [2]
            clicked_row = int(mouse_y) // 200
            clicked_col = int(mouse_x) // 200


            
            if avaible_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2

                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                draw_XO()



    pygame.display.update()