
# This solution was done entirely using Brute Force

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for a in board:
            valid_check = []
            for b in a:
                if b in valid_check:
                    return False
                if b != ".":
                    valid_check.append(b)
                print(valid_check)
        
        for n in range(9):
            valid_check = []
            for m in range(9):
                if board[m][n] in valid_check:
                    return False
                if board[m][n] != ".":               
                    valid_check.append(board[m][n])
                print(valid_check)      

       
        for j in range(3):
            for l in range(3):
                valid_check = []
                for z in range(3):
                    
                    for y in range(3):
                        if board[3*j+z][3*l+y] in valid_check:
                            return False
                        if board[3*j+z][3*l+y] != ".":
                            valid_check.append(board[3*j+z][3*l+y])
                        print(valid_check)
        return True
