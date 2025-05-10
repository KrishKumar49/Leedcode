class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        one = False

        for i in range(n):
            if nums[i] == 1:
                one = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not one:
            return 1

        for i in range(n):
            idx = abs(nums[i])
            nums[idx - 1] = -abs(nums[idx - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
