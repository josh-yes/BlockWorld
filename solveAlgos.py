#!/Users/joshuaschmitz/opt/anaconda3/bin/python3


"""
Josh Schmitz
Machine Learning
HW5

Description:
Implements 3 machine learning algorithms for solving blockworld: smartSolve, bread-first, depth-first
"""


from board import Board


def dfs(board=Board(5, 5), history=[], path=[], depth=25):
    """
    Recursive implementation of dfs for board states.
    
    paramaters
        board: the board whose child states we will evaluate
        history: a list of all the visited states
        path: a list of the path taken to get to the state given in board
        depth: max recursion depth - used to prevent infinite recursion
        
    return
        true if the current state leads to a solution, the path used to get to the solution
    """

    history.append(board)
    path.append(board)
    if board.isSolved():
        return True, path
    if depth == 0:
        return False, path

    for move in board.getValidMoves():
        child = Board(0, 0, board)
        child.moveBlock(move[0], move[1])

        # determine if child has been visited before
        seen = False
        for state in history:
            if child == state:
                seen = True
                break
        
        # if child hasn't been visited
        if not seen:
            solved, newPath = dfs(child, history, [val for val in path], depth - 1)
            if solved:
                return True, newPath
    
    return False, path


def depthFirst(board=Board(5, 5)):
    """
    Starts dfs and prints the solution path.
    """

    print("~~~Depth First Search~~~")

    solved, path = dfs(board)
    
    i = 0
    for state in path:
        print("i: ", i)
        i += 1
        state.printBoard()
        print()


def bfs(tree={}, board=Board(5, 5), history=[]):
    """
    Iterative implementation of bfs for board states.
    
    paramaters
        tree: dictionary of style {board1: parentOfBoard1, board2: parentOfBoard2, initialBoard: -1} - used for determing path to solution
        board: the initial board
        history: holds all the evaluated game states
    
    return
        true if a solution was found, the solved board
    """

    q = [board]
    
    tree[board.toString()] = -1
    history.append(board)
 
    while q:
        curr = q.pop(0)

        if curr.isSolved():
            return True, curr
 
        for move in curr.getValidMoves():
            child = Board(0, 0, curr)
            child.moveBlock(move[0], move[1])

            # determine if child has been visited before
            seen = False
            for state in history:
                if child == state:
                    seen = True
                    break
            
            # if child hasn't been visited
            if not seen:
                history.append(child)
                tree[child.toString()] = curr.toString()
                q.append(child)

    return False


def breadFirst(board=Board(5, 5)):
    """
    Starts bfs and prints the solution path.
    """

    print("~~~Bread First Search~~~")
    
    tree = {}
    solved, state = bfs(tree, board)

    # get the solution path by navigating tree backwards
    path = []
    val = tree[state.toString()]
    path.append(state.toString())
    while val != -1:
        path.append(val)
        val = tree[val]
    
    # print solution path
    i = 0
    while path:
        print("i: ", i)
        i += 1
        print(path.pop())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~ All methods below are used for smartSolve ~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def findBlock(board, block):
    """
    Find the row that block is in for the given board

    paramaters
        board: the board to search through
        block: the integer you are trying to find

    return
        int: the index in board.board that holds the list where block is
    """

    for i in range(board.numPlaces):
        if block in board.board[i]:
            return i


def moveToTarget(board, i, path):
    """
    Move the block i to the third row, usually requires moving the blocks that are in the way back and forth between rows 1 and 2.
    
    paramaters
        board: the board to operate on
        i: the block number you are trying to move to row 3
        path: holds a list of board states representing a path from initial state to the solution
    """

    place = findBlock(board, i)
    
    # move the blocks to the right of i out of the way so i can be moved
    while board.board[place][-1] != i:
        if place == 0:
            board.moveBlock(0, 1)
            path.append(Board(0, 0, board))
        else:
            board.moveBlock(1, -1)
            path.append(Board(0, 0, board))
    
    # move i to row 3
    while place != 2:
        board.moveBlock(place, 1)
        path.append(Board(0, 0, board))
        place += 1


def smartSolve(board=Board(5, 5)):
    """
    An efficient, algorithm for solving block world.
    The idea is to start with block 0 and move it to row 3, then move block 1 to row 3, then block 2, etc until all of the blocks are sorted and on row 3.
    """
    
    print("~~~Smart Solve~~~")

    path = [Board(0, 0, board)]
    for i in range(board.numBlocks):
        moveToTarget(board, i, path)
    
    for state in path:
        state.printBoard()
        print()