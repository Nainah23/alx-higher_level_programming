#!/usr/bin/python3
"""provides a soln to the N-queens puzzle
derives all solns to placing N non-attacking queens on an N×N chessboard

Attributes:
    cboard (list): list array repping the chessboard
    solns (list): list array with the solutions.
"""
import sys

def board_in(n):
    """Chessboard initialization with zeros"""
    cboard = []
    [cboard.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in cboard]
    return (cboard)
def dcopy_board(cboard):
    """Gets the chessboard deep copy"""
    if isinstance(cboard, list):
        return list(map(dcopy_board, cboard))
    return (cboard)

def soln_get(cboard):
    """Gets the list array representation of a chessboard
    thet is solved"""
    soln = []
    for i in range(len(cboard)):
        for j in range(len(cboard)):
            if cboard[i][j] == "Q":
                soln.append([i, j])
                break
        return (soln)

def xplay(cboard, row, column):
    """spots out all places where non-attacking
    queens can't be played

    Args:
        cboard (list): Chessboard
        column (int): last col queen played
        row (int): last row queen played
    """
    for j in range(column + 1, len(cboard)):
        cboard[row][j] = "x"
    for j in range(column - 1, -1, -1):
        cboard[row][j] = "x"
    for i in range(row + 1, len(cboard)):
        cboard[i][column] = "x"
    for i in range(row - 1, -1, -1):
        cboard[i][column] = "x"
    j = column + 1
    for i in range(row + 1, len(cboard)):
        if j >= len(cboard):
            break
        cboard[i][j] = "x"
        j += 1
    j = column - 1
    for i in range(row - 1, -1, -1):
        if j < 0:
            break
        cboard[i][j]
        j -= 1
    j = column + 1
    for i in range(row - 1, -1, -1):
        if j >= len(cboard):
            break
        cboard[i][j] = "x"
        j += 1
    j = column - 1
    for i in range(row + 1, len(cboard)):
        if j < 0:
            break
        cboard[i][j] = "x"
        j -= 1

def r_soln(cboard, row, queens, solns):
    """solves the puzzle recursively
    Args:
        cboard (list): chessboard
        row (int): row
        queens (int): total placed queens
        solns (list) list array of solns
    Return:
        solns
    """
    if queens == len(cboard):
        solns.append(soln_get(cboard))
        return (solns)

    for j in range(len(cboard)):
        if cboard[row][j] == " ":
            tmp_cboard = dcopy_board(cboard)
            tmp_cboard[row][j] = "Q"
            xplay(tmp_cboard, row, j)
            solns = r_soln(tmp_cboard, row + 1, queens + 1, solns)

    return (solns)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
            print ("N must be at least 4")
            sys.exit(1)

    cboard = board_in(int(sys.argv[1]))
    solns = r_soln(cboard, 0, 0, [])
    for sol in solns:
            print(sol)
