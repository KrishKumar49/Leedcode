class Solution:
    def find_next_empty(self, board: List[List[str]]):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    return r, c
        return None, None

    
    def is_valid(self, board: List[List[str]], guess: int, row: int, col: int) -> bool:
        
        row_vals = board[row]
        if guess in row_vals:
            return False
        
        
        col_vals = []
        for i in range(9):
            col_vals.append(board[i][col])
        if guess in col_vals:
            return False

        
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if guess in board[r][c]:
                    return False

        return True 


    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col = self.find_next_empty(board)

        if row is None:
            return True

        for guess in map(str, range(1, 10)):
            if self.is_valid(board, guess, row, col):
                board[row][col] = guess
                if self.solveSudoku(board):
                    return True
                
            board[row][col] = "."
        
        return False


        

# from collections import defaultdict
# class Solution:
#     def solveSudoku(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         rows = [set() for _ in range(9)]
#         cols = [set() for _ in range(9)]
#         boxes = [set() for _ in range(9)]
        
#         empty_cells = []

#         for r in range(9):
#             for c in range(9):
#                 val = board[r][c]

#                 if val == ".":
#                     empty_cells.append((r, c))
#                 else:
#                     rows[r].add(val)
#                     cols[c].add(val)
#                     boxes[(r // 3) * 3 + (c // 3)].add(val)
                

#         def backtract(index):
#             if index == len(empty_cells):
#                 return True

#             r, c = empty_cells[index]
#             b = (r // 3)*3 + (c // 3)

#             for guess in map(str, range(1,10)):
#                 if guess not in rows[r] and guess not in cols[c] and guess not in boxes[b]:
#                     board[r][c] = guess
#                     rows[r].add(guess)
#                     cols[c].add(guess)
#                     boxes[b].add(guess)

#                     if backtract(index + 1):
#                         return True

#                     board[r][c] = "."
#                     rows[r].remove(guess) 
#                     cols[c].remove(guess) 
#                     boxes[b].remove(guess) 
#             return False

#         backtract(0)