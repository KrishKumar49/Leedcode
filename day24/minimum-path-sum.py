from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def helper(m, n):
            if m < 0 or n < 0:
                return float('inf')
            
            if m == 0 and n == 0:
                return grid[0][0] 
            
            down = helper(m-1, n)
            right = helper(m, n-1)
            
            return grid[m][n] + min(down, right)
        return helper(m-1, n-1)
    
    
    
class SolutionMemo:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}
        
        def helper(m, n):
            if m < 0 or n < 0:
                return float('inf')
            
            if m == 0 and n == 0:
                return grid[0][0]
            
            key = str(m) + ',' + str(n)
            if key in memo:
                return memo[key]
            
            down = helper(m-1, n)
            right = helper(m, n-1)
            
            memo[key] = grid[m][n] + min(down, right)
            return memo[key]
        return helper(m-1, n-1)
    
    
    
    
if __name__ == "__main__":
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    solution = Solution()
    print(solution.minPathSum(grid))
    solution_memo = SolutionMemo()
    print(solution_memo.minPathSum(grid))