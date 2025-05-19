class Solution:
    def triangleType(self, nums: List[int]) -> str:

        def check(nums):
            return nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[2] + nums[0] > nums[1]

        if check(nums):
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"

            elif nums[0] != nums[1] and nums[1] != nums[2] and nums[2] != nums[0]:
                return "scalene"
            
            else:
                return "isosceles"

        else:
            return "none"

        