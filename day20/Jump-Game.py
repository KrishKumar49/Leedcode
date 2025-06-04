class Solution:
    def JumpGame(self, nums: list[int]) -> bool:
        n = len(nums)
            
        def jump(i):
            if i == n -1:
                return True
            
            for j in range(1, nums[i] + 1):
                if jump(i + j):
                    return True
            
            return False
        
        return jump(0)
    

    # memoization
    def JumpGame(self, nums: list[int]) -> bool:
        n = len(nums)
        memo = {n -1: True}
        
        def jump(i):
            if i in memo:
                return memo[i]
            
            for j in range(1, nums[i] + 1):
                if jump(i + j):
                    memo[i] = True
                    return True
                
            memo[i] = False
            return False
        
        return jump(0)
    
    
    # greedy 
    
    def JumpGame(self, nums: list[int]) -> bool:
        n = len(nums)
        
        goal = n - 1 
        cur = n - 2

        while cur >= 0:
            if cur + nums[cur] >= goal:
                goal = cur
            
            cur -= 1
        
        return goal == 0
    

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().JumpGame(nums))
    