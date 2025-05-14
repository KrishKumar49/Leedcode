class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def is_valid(row, col, board):
            for i in range(row):
                # col valid
                if board[i][col] == 'Q':
                    return False

                # digonal valid
                # left digonal

                if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                    return False

                # right digonal 

                if col + (row - i) < n and board[i][col+(row - i)] == "Q":
                    return False

            return True

        def backtrack(row, board):
            if row == n:
                result.append([''.join(r) for r in board])
                return 
            
            for col in range(n):
                if is_valid(row, col, board):
                    board[row][col] = "Q"
                    backtrack(row +1, board)
                    board[row][col] = '.'

                
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return result
                

            