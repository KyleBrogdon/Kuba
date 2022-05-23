import pygame
from KubaGame import KubaGame
from constants import *
from board import Board

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
    board = Board()
    # kuba = KubaGame()

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
                piece = board.get_piece(row, col)
                board.move(piece, 2, 0)
                # kuba.select(row, col)
        board.draw(WIN)
        pygame.display.update()
    pygame.QUIT()



main()