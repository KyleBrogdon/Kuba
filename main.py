import pygame
from KubaGame import KubaGame
from constants import *
from board import Board
from game import KubaGame

# pygame setup code citation: https://www.youtube.com/watch?v=vnd3RfeG3NM
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kuba")

def get_position_from_mouse(pos):
    x,y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = KubaGame(WIN)

    while run:
        clock.tick(FPS)

        # if kuba.get_winner() is not None:
        #     print (kuba.get_winner())
        #     run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(pos)

        game.update()

    pygame.QUIT()



main()