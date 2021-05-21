# Kyle Brogdon
# 20 MAY 2021
# Program that creates a KubaGame board, CS 162's final project

class KubaGame:
    """Represents a Kuba game, played by two players"""
    def __init__(self, (Player_a, color_a), (player_b, color_b)):
        """Creates a Kuba game board with two players playing either black or white"""
        self._game_board = [[""] * 7 for x in range(7)]  # initializes a 7x7 game board
        self._game_board[0][0],  self._game_board[0][1],  self._game_board[1][0],  self._game_board[1][1] = "W"
        self._game_board[5][5], self._game_board[5][6], self._game_board[6][5], self._game_board[6][6] = "W"
        self._game_board[5][0], self._game_board[5][1], self._game_board[6][0], self._game_board[6][1] = "B"
        self._game_board[0][5], self._game_board[0][6], self._game_board[1][5], self._game_board[1][6] = "B"
        for y in range(1, 6):
            self._game_board[y][3] = "R"
            self._game_board[3][y] = "R"
        for j in range(2, 5):
            self._game_board[j][2] = "R"
            self._game_board[j][4] = "R"
        pass

    def get_current_turn(self):
        """"""
        pass

    def make_move(self, player_name, coordinates = (), direction):
        """"""
        pass

    def get_winner(self):
        """"""
        pass

    def get_captured(self, player_name):
        """"""
        pass

    def get_marble(self, coordinates = ()):
        """"""
        pass

    def get_marble_count(self):
        """"""
        pass