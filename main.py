import pygame
import sys

pygame.init()

def draw_lines():
    # horizontal line 1
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # horizontal line 2
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # vertical line 1
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # vertical line 2
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 7
LINE_COLOR = (0, 0, 0)
BG_COLOR = (0, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))  
title = pygame.display.set_caption("Tic Tac Toe") 
screen.fill(BG_COLOR)

draw_lines()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()