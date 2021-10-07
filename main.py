#!/Users/joshuaschmitz/opt/anaconda3/bin/python3


"""
Josh Schmitz
Machine Learning
HW5

Description:
Implements 3 machine learning algorithms for solving blockworld: smartSolve, bread-first, depth-first
"""


import solveAlgos
import sys


if "smartSolve" in sys.argv:
    solveAlgos.smartSolve()
if "bfs" in sys.argv:
    solveAlgos.breadFirst()
if "dfs" in sys.argv:
    solveAlgos.depthFirst()
