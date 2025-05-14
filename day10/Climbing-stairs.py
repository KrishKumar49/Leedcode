# class Solution:
#     def climbStairs(self, n: int) -> int:
#             if n == 1:
#                 return 1
#             if n == 2:
#                 return 2

#             prev = 1
#             cur = 2
#             for i in range(2, n):
#                 prev, cur = cur, prev + cur
#             return cur
        
        
        
# recursive solution
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    

# memoization solution

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def f(x: int) -> int:
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x - 1) + f(x - 2)
            return memo[x]
        return f(n)
    
    
# dynamic programming solution

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n-1]
            
            
# dynamic programming solution with space optimization

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev = 1
        cur = 2
        for i in range(2, n):
            prev, cur = cur, prev + cur
        return cur