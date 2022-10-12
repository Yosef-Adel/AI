# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework5
#
# Author(s):
# Yosef Saaid
# Mohamed Gazar
#CUFF_NIGHTMARE
# ----------------------------------------------------------------------
"""
Sudoku puzzle solver implementation

q1:  Basic Backtracking Search
q2:  Backtracking Search with AC-3
q3:  Backtracking Search with MRV Ordering and AC-3
"""
from this import d
import csp
# the constraint function that check the consistency of the new assignment
# if it follows the constraints or not
def constraint(var1, value1, var2, value2):
    if value1 != value2:
        return True
    return False


def domain(puzzle):
    domains = {}
    for row in range(9):
        for col in range(9):
            key = (row, col)
            if key in puzzle:
                domains[(row, col)] = {puzzle[(row, col)]}
            else:
                domains[(row, col)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    return domains

def neighbors():
    neighbors = {}
    for row in range(9):
        for col in range(9):
            key = (row, col)
            neighbors[key] = set()

            for x in range(9):
                if key != (row, x):
                    neighbors[key].add((row, x))
            for x in range(9):
                if key != (x, col):
                    neighbors[key].add((x, col))

            startCol = (col - col % 3)  # 0, 3, 6
            startRow = (row - row % 3)

            for i in range(3):
                for j in range(3):
                    if key != (i + startRow, j + startCol):
                        neighbors[key].add((i + startRow, j + startCol))
    return neighbors




def build_csp(puzzle):
    """
    Create a CSP object representing the puzzle.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: CSP object
    """

    # creating our domain for the 9 * 9 sudoku which is
    # the value that is assigned for the assigned squares and
    # from 1 to 9 for the non-assigned squares
    
    #Our square neighbour is all the squares that is in the same column, row, and 3*3 square
    

    d= domain(puzzle)
    n = neighbors()
    return csp.CSP(d,n,constraint)


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    created_csp = build_csp(puzzle)
    return created_csp.backtracking_search(created_csp), created_csp

def q2(puzzle):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    created_csp = build_csp(puzzle)
    csp.CSP.ac3_algorithm(created_csp)
    return csp.CSP.backtracking_search(created_csp), created_csp

def q3(puzzle):
    """
    Solve the given puzzle with backtracking search and MRV ordering and
    AC-3 as a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    created_csp = build_csp(puzzle)

    csp.CSP.ac3_algorithm(created_csp)

    return csp.CSP.backtracking_search(created_csp, "MRV"), created_csp