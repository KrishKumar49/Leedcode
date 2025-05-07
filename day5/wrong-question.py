class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        h_len = len(haystack)
        left = 0
        right = 0
        count = 0

        for i in range(n_len):
            right += 1
            

        while right != h_len:
            if needle in haystack[left:right+1]:
                count += 1
            left += 1
            right += 1
        return count
