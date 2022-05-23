import pygame
from constants import *
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 8
        self.red_left = 13
        self.create_board()

    def draw_squares(self, win):
        win.fill(GREY)
        for row in range (ROWS):
            for col in range (COLS):
                pygame.draw.rect(win, BLACK, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)


    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece (self, row, col):
        return self.board[row][col]

    def create_board(self):
        # place white in upper left
        for row in range (ROWS):
            self.board.append([])
            for col in range (COLS):
                if (row, col) in BLACK_LIST:
                    self.board[row].append(Piece(row, col, BLACK))
                elif (row, col) in WHITE_LIST:
                    self.board[row].append(Piece(row, col, WHITE))
                elif (row, col) in RED_LIST:
                    self.board[row].append(Piece(row, col, RED))
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def get_valid_moves(self, piece):
        moves = {}


        # place white in lower right
        # place black in upper right
        # place black in lower left
        # place red in center

