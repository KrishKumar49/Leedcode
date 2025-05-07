class Solution:
    def longestPalindrome(self, s: str) -> str:        
        max_len = 0
        start = 0
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i > max_len and self.palindrome(s[i:j]):
                    start = i
                    max_len = j - i

        return s[start:start + max_len]



    def palindrome (self, sb: str) -> bool:
        return sb == sb[::-1]
    


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if not s:
#             return ""

#         def expand(l: int, r: int) -> str:
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 l -= 1
#                 r += 1
#             return s[l+1: r]
#         res = ''
#         for i in range(len(s)):
#             odd = expand(i, i)
#             even = expand(i, i+1)
#             res = max(res,odd,even,key=len)

#         return res
