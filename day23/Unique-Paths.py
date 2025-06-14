class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0
        
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
    

    


class SolutionMemo:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def gridTraveller(m, n):
            if m == 1 and n == 1:
                return 1
            
            if m == 0 or n == 0:
                return 0
            
            key = str(m) + ',' + str(n)
            if key in memo:
                return memo[key]
            
            memo[key] = gridTraveller(m-1, n) + gridTraveller(m, n-1)
            
            return memo[key]
        return gridTraveller(m, n)
    
    



