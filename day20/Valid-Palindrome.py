class Solution:
    def isPalindeome(self, s: str) -> bool:
        cleaner = ''.join([c for c in s.lower() if c.isalnum()])
        return cleaner == cleaner[::-1]