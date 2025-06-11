class Solution:
    def SingleNumber(self, nums: list[int]) -> int:
        counter = {}
        
        for n in nums:
            if n in counter:
                counter[n] += 1
                
            else:
                counter[n] = 1
                
        for key, val in counter.items():
            if val == 1:
                return key