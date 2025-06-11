class Solution:
    def SpriraMatrixGenerator(self, n: int) -> List[List[int]]:
        left, right = 0, n
        top, bottom = 0, n
        
        result = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        
        while left < right and top < bottom:
            for i in range(left, right):
                result[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bottom):
                result[i][right - 1] = num
                num += 1
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            for i in range(right-1, left-1, -1):
                result[bottom -1][i] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom - 1, top - 1, -1):
                result[i][left] = num
                num += 1
            left += 1
            
        return result