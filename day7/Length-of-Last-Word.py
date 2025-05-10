class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = s.split()
        if word[-1] == " ":
            return len(word[-2])
        else:
            return len(word[-1])
