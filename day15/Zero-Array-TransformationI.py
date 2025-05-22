class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        for q in range(len(queries)):
            start = queries[q][0]
            end = queries[q][1]
            
            for i in range(start,end +1):
                nums[i] -= 1


        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        
        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        return True
    
    
    

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        delta = [0] * (N+1)
        # for q in range(len(queries)):
        #     delta[queries[q][0]] += 1
        #     delta[queries[q][1] + 1] -= 1
    

        for l, r in queries:
            delta[l] += 1
            delta[r+1] -= 1

        
        for i in range(1, N+1):
            delta[i] += delta[i-1]

        for i in range(N):
            if nums[i] > delta[i]:
                return False
        
        return True