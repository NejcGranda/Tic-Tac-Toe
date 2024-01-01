import pygame
import sys
import numpy as np
pygame.init()

# nariše črte za križec krožec
def draw_lines():
    # horizontal line 1
    pygame.draw.line(screen, LINE_COLOR, (0, SQARE_SIZE), (WIDTH, SQARE_SIZE), LINE_WIDTH)
    # horizontal line 2
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQARE_SIZE), (WIDTH, 2 * SQARE_SIZE), LINE_WIDTH)

    # vertical line 1
    pygame.draw.line(screen, LINE_COLOR, (SQARE_SIZE, 0), (SQARE_SIZE, HEIGHT), LINE_WIDTH)
    # vertical line 2
    pygame.draw.line(screen, LINE_COLOR, (2 * SQARE_SIZE, 0), (2 * SQARE_SIZE, HEIGHT), LINE_WIDTH)

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
                pygame.draw.circle(screen, O_COLOR, (int(col * SQARE_SIZE + SQARE_SIZE // 2), int(row * SQARE_SIZE + SQARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)

            # player 2 turn
            elif board[row] [col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * SQARE_SIZE + SPACE_SQUARE, row * SQARE_SIZE + SQARE_SIZE - SPACE_SQUARE), (col * SQARE_SIZE + SQARE_SIZE - SPACE_SQUARE, row * SQARE_SIZE + SPACE_SQUARE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * SQARE_SIZE + SPACE_SQUARE, row * SQARE_SIZE + SPACE_SQUARE), (col * SQARE_SIZE + SQARE_SIZE - SPACE_SQUARE, row * SQARE_SIZE + SQARE_SIZE - SPACE_SQUARE), X_WIDTH)

# izpiše zmagovalca
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# preveri za zmagovalca
def win(player):

    # vertical win check
    for col in range(BOARD_COLS):
        if board[0] [col] == player and board[1] [col] == player and board[2] [col] == player:
            draw_vertical_winning_line(col, player)
            draw_text(f"ZMAGAL JE PLAYER{player}", text_font, TEXT_COLOR, WIDTH // 2 - SPACE_BORDER, HEIGHT // 2 - SPACE_BORDER)
            return True
        
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row] [0] == player and board[row] [1] == player and board[row] [2] == player:
            draw_horizontal_winning_line(row, player)
            draw_text(f"ZMAGAL JE PLAYER{player}", text_font, TEXT_COLOR, WIDTH // 2 - SPACE_BORDER, HEIGHT // 2 - SPACE_BORDER)
            return True
        
    # asc diagonal win check
    if board[2] [0] == player and board[1] [1] == player and board[0] [2] == player:
        draw_asc_diagonal(player)
        draw_text(f"ZMAGAL JE PLAYER{player}", text_font, TEXT_COLOR, WIDTH // 2 - SPACE_BORDER, HEIGHT // 2 - SPACE_BORDER)
        return True
    
    # desc diagonal win check
    if board[0] [0] == player and board[1] [1] == player and board[2] [2] == player:
        draw_desc_diagonal(player)
        draw_text(f"ZMAGAL JE PLAYER{player}", text_font, TEXT_COLOR, WIDTH // 2 - SPACE_BORDER, HEIGHT // 2 - SPACE_BORDER)
        return True
    
    return False

# nariše vodoravno črto zmagovalcu
def draw_vertical_winning_line(col, player):
    pos_x = col * SQARE_SIZE + SQARE_SIZE // 2

    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), WINNING_LINE_WIDTH)

# nariše navpično črto zmagovalcu
def draw_horizontal_winning_line(row, player):
    pos_y = row * SQARE_SIZE + SQARE_SIZE // 2

    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), WINNING_LINE_WIDTH)

# nariše naraščujočo diagonalno črto zmagovalcu
def draw_asc_diagonal(player):
    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WINNING_LINE_WIDTH)

# nariše padajočo diagonalno črto zmagovalcu
def draw_desc_diagonal(player):
    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WINNING_LINE_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[col] [row] = 0


WIDTH = 900
HEIGHT = WIDTH

LINE_WIDTH = 7
X_WIDTH = 25
WINNING_LINE_WIDTH = 15

BOARD_ROWS = 3
BOARD_COLS = 3

SQARE_SIZE = WIDTH // BOARD_COLS

SPACE_SQUARE = SQARE_SIZE // 4
SPACE_BORDER = WIDTH // 4 + 100

CIRCLE_RADIUS = SQARE_SIZE // 3
CIRCLE_WIDTH = 15


# colors
LINE_COLOR = (0, 0, 0)
BG_COLOR = (0, 255, 255)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)
TEXT_COLOR = (100, 100, 100)

text_font = pygame.font.SysFont("Arial", WIDTH // 12)

screen = pygame.display.set_mode((WIDTH, HEIGHT))  
title = pygame.display.set_caption("Tic Tac Toe") 
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

player = 1


draw_lines()
game_over = False


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]


            # izračuna pozicijo kvadratkov v [0] [1] [2]
            clicked_row = int(mouse_y) // SQARE_SIZE
            clicked_col = int(mouse_x) // SQARE_SIZE

            
            if avaible_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if win(player):
                    game_over = True
                player = player % 2 + 1

                draw_XO()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False


    pygame.display.update()