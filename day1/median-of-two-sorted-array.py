class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr = sorted(arr)

        left = 0
        right = len(arr) - 1
        while left < right :
            left = left + 1
            right = right - 1
        if left == right :
            return float(arr[left])
        else :
            return (arr[left] + arr[right]) / 2.0