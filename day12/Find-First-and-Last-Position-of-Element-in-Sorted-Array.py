# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             if nums[left] == target and nums[right] == target:
#                 return [left, right]

#             elif nums[left] != target and nums[right] == target:
#                 left += 1

#             elif nums[left] == target and nums[right] != target:
#                 right -= 1
#             else:
#                 left += 1
#                 right -= 1

#         return [-1, -1]


# Time Complexity: O(n)


# -------------------------------------------

