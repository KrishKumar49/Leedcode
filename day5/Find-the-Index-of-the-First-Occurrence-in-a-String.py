class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        h_len = len(haystack)
        left = 0
        right = n_len
            
        while right <= h_len:
            if needle in haystack[left:right]:
                return left
            left += 1
            right += 1
        return -1
