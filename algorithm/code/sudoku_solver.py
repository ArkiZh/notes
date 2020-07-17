"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:
The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self._dfs(board,0,0)
        return board

    def solveSudokuAll(self, board):
        self.all_solutions = []
        self.counter = 0
        self._dfs_findall(board,0,0)
        return self.all_solutions
    
    def _dfs_findall(self,board,row,col):
        if row == len(board):
            self.all_solutions.append(board.copy())
            self.counter+=1
            print("---------- %d ----------"%self.counter)
            self._print(board)
            return

        row_new, col_new = (row+1, 0) if col==8 else (row, col+1)

        if board[row][col]==".":
            # self._print(board)
            black = 0
            for i in range(9):
                for temp in (board[row][i],board[i][col],board[row//3*3+i//3][col//3*3+i%3]):
                    if temp!=".":
                        black = black | 1<<int(temp)-1
            cnt = 1
            candidates = 0b111111111 ^ black
            # print("(%d, %d)"%(row,col),bin(black),"->",bin(candidates))
            
            if candidates==0:
                return
            while candidates!=0:
                if candidates&1:
                    # print(bin(candidates))
                    board[row][col] = str(cnt)
                    self._dfs_findall(board, row_new, col_new)
                    board[row][col]="."
                cnt+=1
                candidates>>=1
        else:
            self._dfs_findall(board, row_new, col_new)
                    
                        

    def _dfs(self, board, row, col):
        if row == len(board):
            # print("ENDENDEND")
            # self._print(board)
            # print("ENDENDEND")
            return True

        # Next position
        if col == len(board)-1:
            row_new, col_new = row+1, 0
        else:
            row_new, col_new = row, col+1
        # print("(%d,%d)->(%d,%d) at %s"%(row,col,row_new,col_new,board[row][col]))
        # Choose value
        if board[row][col] == ".":
            candidates = {str(i) for i in range(1, 10)}

            # valid row
            candidates = candidates-{x for x in board[row]}
            # valid col
            candidates = candidates-{x[col] for x in board}
            # valid grid
            candidates = candidates-{board[row//3*3+i][col//3*3+j] for i in range(3) for j in range(3)}
            if len(candidates)==0:
                return False
            for c in candidates:
                board[row][col]=c
                # Move forward
                retval = self._dfs(board,row_new,col_new)
                if retval:
                    return retval
                board[row][col]="."
                    
        else:
            # Move forward
            return self._dfs(board,row_new,col_new)
                    
    def _print(self, board):
        for row in board:
            print(" ".join(row))
                


            
sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sudoku = [["."]*9 for i in range(9)]
print("Origin:")
for row in sudoku:
    print(" ".join(row))
print("result:")
for row in Solution().solveSudoku(sudoku):
    print(" ".join(row))

sudoku = [["."]*9 for i in range(9)]



sudoku[0][0:3] = ["5","2","1"]
sudoku[1][3:6] = ["5","2","1"]
sudoku[2][6:9] = ["5","2","1"]

sudoku[3][1:4] = ["5","2","1"]
sudoku[4][4:7] = ["5","2","1"]
sudoku[5][7:9] = ["5","2"]
sudoku[5][0] = "1"

sudoku[6][2:5] = ["5","2","1"]
sudoku[7][5:8] = ["5","2","1"]
sudoku[8][8] = "5"
sudoku[8][0:2] = ["2","1"]


for row in sudoku:
    print(" ".join(row))

print("All results:")
for result in Solution().solveSudokuAll(sudoku.copy()):
    print("-"*9)
    for row in result:
        print(" ".join(row))
print("END")
