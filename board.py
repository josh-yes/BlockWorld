#!/Users/joshuaschmitz/opt/anaconda3/bin/python3


"""
Josh Schmitz
Machine Learning
HW4

Description:
I will be making a block world and generating random moves.
"""


import random


class Board():
    """
    Keep track of game state for a board. Places are 0 to (numPlaces - 1). Blocks are 0 to (numBlocks - 1).
    """

    def __init__(self, numPlaces, numBlocks, otherBoard=None):
        """
        Create new board. If otherBoard is given it will be copied, otherwise a random initial board will be made.

        paramaters
            numPlaces: the number of places for the board
            numBlocks: the number of blocks on the board
            other: 
        """

        if otherBoard is None: # Default constructor
            self.board = [[] for i in range(numPlaces)]
            self.numBlocks = numBlocks
            self.numPlaces = numPlaces

            l = [i for i in range(numBlocks)]
            while len(l) > 0:
                num = random.choice(l)
                l.remove(num)
                self.board[0].append(num)
        else: # copy constructor
            self.board = []
            self.numBlocks = otherBoard.numBlocks
            self.numPlaces = otherBoard.numPlaces

            for place in otherBoard.board:
                self.board.append([place[i] for i in range(len(place))])
            

    def __eq__(self, other):
        """
        == override
        
        paramaters
            other: the board you're comparing to self
            
        return
            true if self == board else false
        """

        if self.numBlocks != other.numBlocks or self.numPlaces != other.numPlaces:
            return False
        for i in range(self.numPlaces):
            if len(self.board[i]) != len(other.board[i]):
                return False
            for j in range(len(self.board[i])):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True


    def printBoard(self):
        """
        Print current board state.
        """

        for place in self.board:
            print("|", place)

    
    def toString(self):
        """
        Makes a string representing the current board state. The string is in the same format as the printBoard() method produces.
        
        return
            string: the string representing the current board state
        """
        
        string = ""
        for place in self.board:
            string += "|" + str(place) + "\n"
        return string


    def moveBlock(self, place, direction):
        """
        Move the top block on place to the left or right.

        paramaters
            place: the place you want to move a block from
            direction: the direction you want to move (1 for forward or -1 for backwards)
        """

        newPlace = place + direction
        num = self.board[place].pop()
        self.board[newPlace].append(num)


    def getValidMoves(self):
        """
        Get a list of valid moves for the current board state.
        
        return
            moves: all of the valid moves represented by a list of lists like [place, direction]
        """

        moves = []
        for i in range(self.numPlaces):
            if self.board[i] == []:
                continue
            elif i == 0:
                moves.append([i, 1])
            elif i == self.numPlaces - 1:
                moves.append([i, -1])
            else:
                moves.append([i, -1])
                moves.append([i, 1])
        return moves


    def randomMove(self):
        """
        Make a random move.
        """
        
        moves = self.getValidMoves()
        move = random.choice(moves)
        self.moveBlock(move[0], move[1])

    
    def isSolved(self):
        """
        Checks if the board is solved.
        
        return
            True if it's solved else false
        """
        
        for place in self.board:
            if len(place) > 0:
                if len(place) < self.numBlocks:
                    return False
                return all(place[i] <= place[i + 1] for i in range(len(place) - 1)) # checks if 'place' is sorted

