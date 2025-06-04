class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n =  len(matrix)
        def transpose(matrix):
            for r in range(n):
                for c in range(r+1, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

            return matrix

        def reverse(matrix):
            for r in range(n):
                left = 0
                right = n - 1
                while left < right:
                    matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                    left += 1
                    right -= 1
            return matrix

        transpose(matrix)
        reverse(matrix)
        return matrix