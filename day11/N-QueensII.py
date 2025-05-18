class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        def is_valid(row, col, board):
            for i in range(row):
                if board[i][col] == "Q":
                    return False

                if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
                    return False

                if col + (row - i) < n and board[i][col + (row - i)] == "Q":
                    return False

            return True


        def backtrack(row, board):
            if row == n:
                result.append([''.join(r) for r in board])
                return 
            
            for col in range(n):
                if is_valid(row, col, board) :
                    board[row][col] = "Q"
                    backtrack(row+1, board)
                    board[row][col] = "."


        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return len(result)