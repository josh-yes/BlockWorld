#!/Users/joshuaschmitz/opt/anaconda3/bin/python3


"""
Josh Schmitz
Machine Learning
HW5

Description:
Implements 3 machine learning algorithms for solving blockworld: smartSolve, bread-first, depth-first
"""


import solveAlgos
from board import Board
import sys

board = Board(5, 5)
if "smartSolve" in sys.argv:
    solveAlgos.smartSolve(Board(0, 0, board))
if "bfs" in sys.argv:
    solveAlgos.breadFirst(Board(0, 0, board))
if "dfs" in sys.argv:
    solveAlgos.depthFirst(Board(0, 0, board))
