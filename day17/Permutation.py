class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        result = []

        for i in range(len(nums)):
            m = nums[i]
            rem_num = nums[:i] + nums[i+1:]

            for p in self.permute(rem_num):
                result.append([m] + p)
            
        return result





class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        sol = []

        def backtrack(start):
            if len(nums) == start:
                result.append(nums[:])
                return 
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return result