#!/Users/joshuaschmitz/opt/anaconda3/bin python3
"""
Josh Schmitz
Machine Learning
HW5

Description:
Implements 3 machine learning algorithms for solving blockworld: a*, bread-first, depth-first
"""

from board import Board

def getReverseMove(move):
    reverseMove = [0, 0]

    if move[1] == 1:
        reverseMove[1] = -1
        reverseMove[0] = move[0] + 1
    else:
        reverseMove[1] = 1
        reverseMove[0] = move[0] - 1


def dfs(board=Board(5, 5), history=[], depth=50):
    history.append(board)
    if board.isSolved():
        return True
    if depth == 0:
        return False

    for move in board.getValidMoves():
        child = Board(0, 0, board)
        child.moveBlock(move[0], move[1])

        seen = False
        for state in history:
            if child == state:
                seen = True
                break
        
        if not seen:
            if dfs(child, history, depth - 1):
                return True
    return False

def depthFirst():
    print("~~~Depth First Search~~~")
    board = Board(5, 5)
    board.printBoard()
    print()
    history = []
    dfs(board, history)
    history[-1].printBoard()
    print()


def bfs(board=Board(5, 5), history=[]):
    q = [board]
 
    history.append(board)
 
    while q:
        curr = q.pop(0)

        if curr.isSolved():
            return True, curr
 
        for move in curr.getValidMoves():
            child = Board(0, 0, curr)
            child.moveBlock(move[0], move[1])

            seen = False
            for state in history:
                if child == state:
                    seen = True
                    break
            
            if not seen:
                history.append(child)
                q.append(child)

    return False


def breastFirst():
    print("~~~Bread First Search~~~")
    history = []
    board = Board(5, 5)
    board.printBoard()
    print()
    solved, state = bfs(board, history)
    state.printBoard()
    print()


def findBlock(board, block):
    for i in range(board.numPlaces):
        if block in board.board[i]:
            return i


def moveToTarget(board, i):
    place = findBlock(board, i)
    while board.board[place][-1] != i:
        if place == 0:
            board.moveBlock(0, 1)
        else:
            board.moveBlock(1, -1)
    while place != 2:
        board.moveBlock(place, 1)
        place += 1


def smartSolve():
    print("~~~Smart Solve~~~")
    board = Board(5, 5)
    board.printBoard()
    print()
    for i in range(board.numBlocks):
        moveToTarget(board, i)
    board.printBoard()
    print()

smartSolve()
breastFirst()
depthFirst()