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
        self._player_a_color = player_a_tuple[1]  # assign the second value in the tuple to be player a's color
        self._player_b = player_b_tuple[0]  # assign the first value in the tuple to player b's name
        self._player_b_color = player_b_tuple[1]  # assign the second value in the tuple to be player b's color
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
        self._current_roworcolumn = []

    def get_current_turn(self):
        """Returns the player whose turn it is to make a move"""
        return self._current_turn

    def make_move(self, playername, coordinates, direction):
        """Takes a player name, a tuple containing coordinates on the game board of the marble the
        player wishes to move, and the direction (L for left, R for right, F for forward, and B for backwards) the
        player wishes to move that marble. This method will check that moves are valid in accordance with the rules,
        then update the game board, check if the move resulted in a winner for the game, and then set
        the next turn to the other player"""
        if self._game_winner == None:
            if self._current_turn is None or self._current_turn == playername:
                if coordinates[0] < 7 and coordinates[0] >= 0:  # check if coordinates are on the game board
                    if coordinates[1] < 7 and coordinates[1] >= 0: # check if coordinates are on the game board
                        if self.get_player_color(playername) == self.get_marble(coordinates):  # if player is moving his own color marble
                            if direction == "L":
                                return self.make_move_left(playername, coordinates)
                            if direction == "R":
                                return self.make_move_right(playername, coordinates)
                            if direction == "B":
                                return self.make_move_backwards(playername, coordinates)
                            if direction == "F":
                                return self.make_move_forwards(playername, coordinates)
                            return False  # invalid direction was passed
                        return False  # player is not moving his own color marble
                    return False  # coordinates are off the game board
                return False  # coordinates are off the game board
            return False  # not the correct player's turn
        return False  # someone has already won the game

    def make_move_left(self, playername, coordinates):
        """Helper method that moves marbles to the left by taking the playername and coordinates passed to make_move"""
        row = coordinates[0]
        column = coordinates[1]
        previous_board = []
        if column == 6 or self.get_marble((row, column + 1)) == "X":  # if marble is on the edge of the board or the space behind marble is empty
            for x in range(0, 7):
                temp_move = self.get_marble((row, x))
                previous_board.append(temp_move)
            for i in range(column, -1, -1):
                if self.get_marble((row, i)) == "X":
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while counter + i < column:
                        proposed_move[i + counter] = proposed_move[i + increment]
                        counter += 1
                        increment += 1
                    proposed_move[column] = "X"
                    if proposed_move == self._current_roworcolumn:  # violates Ko rule by checking if move would result in same board as last turn
                        return False
                    for a in range(0, 7):
                        self._game_board[row][a] = proposed_move[a]  # update values in that row
                    self._current_roworcolumn = previous_board  # stores previous board to check for ko violation on future move
                    if self._player_a == playername:  # set next turn to appropriate player
                        if self.possible_moves_checker(self._player_b) is False:
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b
                        return True
                    else:
                        if self.possible_moves_checker(self._player_a) is False:
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a
                        return True
                if i == 0:  # if there are marbles lined up till edge of the board and one will get pushed off by this move
                    marble_getting_knocked_off = previous_board[0]
                    if self.get_player_color(playername) == marble_getting_knocked_off:
                        return False  # player cannot knock off their own marble
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while counter + i < column:
                        proposed_move[i + counter] = proposed_move[i + increment]
                        counter += 1
                        increment += 1
                    proposed_move[column] = "X"
                    for b in range(0, 7):
                        self._game_board[row][b] = proposed_move[b]
                    self._current_roworcolumn = previous_board
                    if self._player_a == playername:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_a_captured += 1  # increment captured total
                            if self._player_a_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_a
                            if self.possible_moves_checker(self._player_b) is False:  # check if this move leaves opponent with no valid moves and set winner
                                self._game_winner = self._player_a
                        self._current_turn = self._player_b  # set turn to other player
                        return True
                    else:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_b_captured += 1  # increment captured total
                            if self._player_b_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_b
                            if self.possible_moves_checker(self._player_a) is False:  # check if this move leaves opponent with no valid moves and set winner
                                self._game_winner = self._player_b
                        self._current_turn = self._player_a  # set turn to other player
                        return True
        return False  # not a valid move since the marble is blocked

    def make_move_right(self, playername, coordinates):
        """Helper method that moves marbles to the right by taking the playername and coordinates passed to make_move"""
        row = coordinates[0]
        column = coordinates[1]
        previous_board = []
        if column == 0 or self.get_marble((row, column - 1)) == "X":  # if marble is on the edge of the board or the space behind marble is empty
            for x in range(0, 7):
                temp_move = self.get_marble((row, x))
                previous_board.append(temp_move)
            for i in range(column, 7):
                if self.get_marble((row, i)) == "X":
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while i - counter > column:
                        proposed_move[i - counter] = proposed_move[i - increment]
                        counter += 1
                        increment += 1
                    proposed_move[column] = "X"
                    if proposed_move == self._current_roworcolumn:  # violates Ko rule by checking if move would result in same board as last turn
                        return False
                    for a in range(0, 7):
                        self._game_board[row][a] = proposed_move[a]  # update values in that row
                    self._current_roworcolumn = previous_board  # stores previous board to check for ko violation on future move
                    if self._player_a == playername:  # set next turn to appropriate player
                        if self.possible_moves_checker(self._player_b) is False:
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b
                        return True
                    else:
                        if self.possible_moves_checker(self._player_a) is False:
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a
                        return True
                if i == 6:  # if there are marbles lined up till edge of the board and one will get pushed off by this move
                    marble_getting_knocked_off = previous_board[6]
                    if self.get_player_color(playername) == marble_getting_knocked_off:
                        return False  # player cannot knock off their own marble
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while i - counter > column:
                        proposed_move[i - counter] = proposed_move[i - increment]
                        counter += 1
                        increment += 1
                    proposed_move[column] = "X"
                    for b in range(0, 7):
                        self._game_board[row][b] = proposed_move[b]
                        self._current_roworcolumn = previous_board
                    if self._player_a == playername:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_a_captured += 1  # increment captured total
                            if self._player_a_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_a
                        if self.possible_moves_checker(self._player_b) is False:  # check if this move leaves opponent with no valid moves and set winner
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b  # set turn to other player
                        return True
                    else:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_b_captured += 1  # increment captured total
                            if self._player_b_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_b
                        if self.possible_moves_checker(self._player_a) is False: # check if this move leaves opponent with no valid moves and set winner
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a  # set turn to other player
                        return True
        return False  # not a valid move since the marble is blocked

    def make_move_backwards(self, playername, coordinates):
        """Helper method that moves marbles backwards by taking the playername and coordinates passed to make_move"""
        row = coordinates[0]
        column = coordinates[1]
        previous_board = []
        if row == 0 or self.get_marble((row - 1, column)) == "X":  # if marble is on the edge of the board or the space behind marble is empty
            for x in range(0, 7):
                temp_move = self.get_marble((x, column))
                previous_board.append(temp_move)
            for i in range(row, 7):
                if self.get_marble((i, column)) == "X":
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while i - counter > row:
                        proposed_move[i - counter] = proposed_move[i - increment]
                        counter += 1
                        increment += 1
                    proposed_move[row] = "X"
                    if proposed_move == self._current_roworcolumn:  # violates Ko rule by checking if move would result in same board as last turn
                        return False
                    for a in range(0, 7):
                        self._game_board[a][column] = proposed_move[a]  # update values in that row
                    self._current_roworcolumn = previous_board  # stores previous board to check for ko violation on future move
                    if self._player_a == playername:  # set next turn to appropriate player
                        if self.possible_moves_checker(self._player_b) is False:
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b
                        return True
                    else:
                        if self.possible_moves_checker(self._player_a) is False:
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a
                        return True
                if i == 6:  # if there are marbles lined up till edge of the board and one will get pushed off by this move
                    marble_getting_knocked_off = previous_board[6]
                    if self.get_player_color(playername) == marble_getting_knocked_off:
                        return False  # player cannot knock off their own marble
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while i - counter > row:
                        proposed_move[i - counter] = proposed_move[i - increment]
                        counter += 1
                        increment += 1
                    proposed_move[row] = "X"
                    for b in range(0, 7):
                        self._game_board[b][column] = proposed_move[b]
                        self._current_roworcolumn = previous_board
                    if self._player_a == playername:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_a_captured += 1  # increment captured total
                            if self._player_a_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_a
                        if self.possible_moves_checker(self._player_b) is False:  # check if this move leaves opponent with no valid moves and set winner
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b  # set turn to other player
                        return True
                    else:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_b_captured += 1  # increment captured total
                            if self._player_b_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_b
                        if self.possible_moves_checker(self._player_a) is False:  # check if this move leaves opponent with no valid moves and set winner
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a  # set turn to other player
                        return True
        return False  # not a valid move since the marble is blocked

    def make_move_forwards(self, playername, coordinates):
        """Helper method that moves marbles forward by taking the playername and coordinates passed to make_move"""
        row = coordinates[0]
        column = coordinates[1]
        previous_board = []
        if row == 6 or self.get_marble((row + 1, column)) == "X":  # if marble is on the edge of the board or the space behind marble is empty
            for x in range(0, 7):
                temp_move = self.get_marble((x, column))
                previous_board.append(temp_move)
            for i in range(row, -1, -1):
                if self.get_marble((i, column)) == "X":
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while counter + i < row:
                        proposed_move[i + counter] = proposed_move[i + increment]
                        counter += 1
                        increment += 1
                    proposed_move[row] = "X"
                    if proposed_move == self._current_roworcolumn:  # violates Ko rule by checking if move would result in same board as last turn
                        return False
                    for a in range(0, 7):
                        self._game_board[a][column] = proposed_move[a]  # update values in that row
                    self._current_roworcolumn = previous_board  # stores previous board to check for ko violation on future move
                    if self._player_a == playername:  # set next turn to appropriate player
                        if self.possible_moves_checker(self._player_b) is False:
                            self._game_winner = self._player_a
                        self._current_turn = self._player_b
                        return True
                    else:
                        if self.possible_moves_checker(self._player_a) is False:
                            self._game_winner = self._player_b
                        self._current_turn = self._player_a
                        return True
                if i == 0:  # if there are marbles lined up till edge of the board and one will get pushed off by this move
                    marble_getting_knocked_off = previous_board[0]
                    if self.get_player_color(playername) == marble_getting_knocked_off:
                        return False  # player cannot knock off their own marble
                    proposed_move = list(previous_board)
                    counter = 0
                    increment = 1
                    while counter + i < row:
                        proposed_move[i + counter] = proposed_move[i + increment]
                        counter += 1
                        increment += 1
                    proposed_move[row] = "X"
                    for b in range(0, 7):
                        self._game_board[b][column] = proposed_move[b]
                        self._current_roworcolumn = previous_board
                    if self._player_a == playername:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_a_captured += 1  # increment captured total
                            if self._player_a_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_a
                            if self.possible_moves_checker(
                                    self._player_b) is False:  # check if this move leaves opponent with no valid moves and set winner
                                self._game_winner = self._player_a
                        self._current_turn = self._player_b  # set turn to other player
                        return True
                    else:
                        if marble_getting_knocked_off == "R":  # check if the marble is red and will score points
                            self._player_b_captured += 1  # increment captured total
                            if self._player_b_captured == 7:  # Check if player has won the game and set winner
                                self._game_winner = self._player_b
                            if self.possible_moves_checker(
                                    self._player_a) is False:  # check if this move leaves opponent with no valid moves and set winner
                                self._game_winner = self._player_b
                        self._current_turn = self._player_a  # set turn to other player
                        return True
        return False  # not a valid move since the marble is blocked

    def possible_moves_checker(self, playername):
        """Helper method that checks if the opposing player can make any valid moves"""
        pass


    def get_winner(self):
        """Returns the current status of the winner of the game"""
        return self._game_winner

    def get_captured(self, playername):
        """Takes a player name and returns the number of red marbles captured by the player"""
        if self._player_a == playername:  # checks to see which player we are returning the value for
            return self._player_a_captured
        else:
            return self._player_b_captured

    def get_marble(self, coordinates):
        """Takes a coordinate tuple and returns the value at the coordinate, which is
        either a red, black, white marble, or 'X' for no marble"""
        x = coordinates[0]
        y = coordinates[1]
        return self._game_board[x][y]  # returns the value at the correct coordinates on the board

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

    def get_player_color(self, playername):
        """Takes a player name and returns what color they are playing with"""
        if self._player_a == playername:  # checks to see which player we are returning the value for
            return self._player_a_color
        else:
            return self._player_b_color

# game = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
# print(game.get_marble_count()) #returns (8,8,13)
# print(game.get_captured('PlayerA')) #returns 0
# game.get_current_turn() #returns 'PlayerB' because PlayerA has just played.
# print(game.get_winner()) #returns None
# print(game.make_move('PlayerA', (6,5), 'F'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerB', (5,0), 'R'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerA', (5,5), 'F'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerB', (5,1), 'R'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerA', (4,5), 'F'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerB', (5,2), 'R'))
# print(game.make_move('PlayerA', (3,5), 'F')) # irrelevant
# print(game.make_move('PlayerB', (5,3), 'R'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.make_move('PlayerB', (5,3), 'R'))
# print(game.make_move('PlayerA', (2,5), 'F'))
# print(game.make_move('PlayerB', (5,4), 'R'))
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.get_marble_count()) #returns (8,7,13)
# print(game.get_captured('PlayerA'))
# print(game.get_captured('PlayerB'))
# print(game.make_move('PlayerB', (4,0), ''))
# print(game.make_move('PlayerA', (4,6), 'L'))
# print(game.make_move('PlayerB', (3,0), 'L'))
# game.get_marble((5,5)) #returns 'W'
