import pygame
from constants import *

class Piece:
    PADDING = 20
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # self.direction  = 1
        self.x = 0
        self.y = 0
        self.calc_pos()


    def calc_pos(self):
        # Calculate X and add square // 2 to make sure it is in the center of the square
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        # Calculate y and add square // 2 to make sure it is in the center of the square
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        RADIUS = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, BLACK, (self.x, self.y), RADIUS + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS)


    def move (self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
