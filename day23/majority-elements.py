class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
                
        for key, val in counter.items():
            if val > (len(nums) // 2):
                return key
    
