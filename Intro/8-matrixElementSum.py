# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr/drafts
# Level 2: Intro - Edge of the Ocean

"""
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room,
your task is to return the total sum of all rooms that are suitable for the CodeBots
(ie: add up all the values that don't appear below a 0).
"""


def solution(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    total = 0
    
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] != 0:
                if i != 0 and matrix[i-1][j] == 0:
                    matrix[i][j] = 0
                if (i!= 0 and matrix[i-1][j] != 0) or i == 0:
                    total += matrix[i][j]
                
    return total
