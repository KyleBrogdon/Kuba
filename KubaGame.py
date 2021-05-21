# Kyle Brogdon
# 20 MAY 2021
# Program that creates a KubaGame board, CS 162's final project

class KubaGame:
    """Represents a Kuba game, played by two players"""
    def __init__(self, player_a_tuple, player_b_tuple):
        """Creates a 7x7 Kuba game board with two players playing either black marbles or white marbles by taking a tuple
        containing each player's name and color, sets current turn to None, sets game winner to None, and sets
        each player's red marble captured count to 0"""
        self._player_a = player_a_tuple[0]  # assign the first value in the tuple to player a's name
        self.player_a_color = player_a_tuple[1]  # assign the second value in the tuple to be player a's color
        self.player_b = player_b_tuple[0]  # assign the first value in the tuple to player b's name
        self.player_b_color = player_b_tuple[1]  # assign the second value in the tuple to be player b's color
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
        for y in range(1, 6):  # iterate through to put red marbles at correct positions
            self._game_board[y][3] = "R"  # "R" represents red marbles
            self._game_board[3][y] = "R"
        for j in range(2, 5):  # iterate through to put red marbles at correct positions
            self._game_board[j][2] = "R"
            self._game_board[j][4] = "R"
        self._current_turn = None  # initializes current turn to None as either player can start the game
        self._game_winner = None  # initializes game winner to None since game has not started
        self._player_a_captured = 0  # sets each player's captured red marble count to 0
        self._player_b_captured = 0  # sets each player's captured red marble count to 0

    def get_current_turn(self):
        """Returns the player whose turn it is to make a move"""
        return self._current_turn

    def make_move(self, playername, coordinates, direction):
        """Takes a player name, a tuple containing coordinates on the game board of the marble the
        player wishes to move, and the direction (L for left, R for right, F for forward, and B for backwards) the
        player wishes to move that marble. This method will check that moves are valid in accordance with the rules,
        then update the game board, check if the move resulted in a winner for the game, and then set
        the next turn to the other player"""
        pass

    def get_winner(self):
        """Returns the current status of the winner of the game"""
        return self._game_winner

    def get_captured(self, player_name):
        """Takes a player name and returns the number of red marbles captured by the player"""
        if self._player_a == player_name:
            return self._player_a_captured
        else:
            return self._player_b_captured

    def get_marble(self, coordinates):
        """Takes a coordinate tuple and returns the value at the coordinate, which is
        either a red, black, white marble, or 'X' for no marble"""
        x = coordinates[0]
        y = coordinates[1]
        return self._game_board[x][y]

    def get_marble_count(self):
        """Iterates over the entire game board, counts the number of each color of marble, and
        returns a tuple consisting of white, black, red marbles left on the game board"""
        W = 0  # number of white marbles
        B = 0  # number of black marbles
        R = 0  # number of red marbles
        for x in range(0,7):
            for y in range(0,7):  # iterates through entire 7x7 board
                if self._game_board[x][y] == "W":  # if marble is white, increment white
                    W += 1
                if self._game_board[x][y] == "B":  # if marble is black, increment black
                    B += 1
                if self._game_board[x][y] == "R":  # if marble is red, increment red
                    R += 1
        return(W, B, R)  # returns the tuple of white, black, red marbles