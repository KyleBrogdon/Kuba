# Kyle Brogdon
# 20 MAY 2021
# Program that creates a KubaGame board, CS 162's final project

class KubaGame:
    """Represents a Kuba game, played by two players"""
    def __init__(self, player_a_tuple, player_b_tuple):
        """Creates a 7x7 Kuba game board with two players playing either black marbles or white marbles by taking a tuple
        for each player's name and color, sets current turn to None, sets game winner to None, and sets
        each player's red marble captured count to 0"""
        self._player_a = player_a_tuple[0]
        self.player_a_color = player_a_tuple[1]
        self.player_b = player_b_tuple[0]
        self.player_b_color = player_b_tuple[1]
        # initializes a 7x7 game board, top left corner is 0,0, bottom right is 6,6
        self._game_board = [['X'] * 7 for x in range(7)]  # 'X' represents no marble or an empty space
        self._game_board[0][0],  self._game_board[0][1],  \
        self._game_board[1][0],  self._game_board[1][1] = "W", "W", "W", "W"  # "W" represents white marbles
        self._game_board[5][5], self._game_board[5][6], \
        self._game_board[6][5], self._game_board[6][6] = "W", "W", "W", "W"
        self._game_board[5][0], self._game_board[5][1], \
        self._game_board[6][0], self._game_board[6][1] = "B", "B", "B", "B"  # "B" represents black marbles
        self._game_board[0][5], self._game_board[0][6], \
        self._game_board[1][5], self._game_board[1][6] = "B", "B", "B", "B"
        for y in range(1, 6):
            self._game_board[y][3] = "R"
            self._game_board[3][y] = "R"
        for j in range(2, 5):
            self._game_board[j][2] = "R"
            self._game_board[j][4] = "R"
        self._current_turn = None  # initializes current turn to None as either player can start the game
        self._game_winner = None  # initializes game winner to None since game has not started
        self._player_a_captured = 0  # sets each player's captured red marble count to 0
        self._player_b_captured = 0  # sets each player's captured red marble count to 0

    def get_current_turn(self):
        """Returns the player whose turn it is to make a move"""
        return self._current_turn

    def make_move(self, player_name, coordinates, direction):
        """"""
        pass

    def get_winner(self):
        """Returns the current status of the winner of the game"""
        return self._game_winner

    def get_captured(self, player_name):
        """Returns the number of red marbles captured by the player"""
        if self._player_a == player_name:
            return self._player_a_captured
        else:
            return self._player_b_captured


    def get_marble(self, coordinates):
        """Returns the value at the coordinate, which is either a red, black, white marble, or 'X' for no marble"""
        x = coordinates[0]
        y = coordinates[1]
        return self._game_board[x][y]

    def get_marble_count(self):
        """"""
        W = 0
        B = 0
        R = 0
        pass