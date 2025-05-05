class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000}
        prev = 0

        for i in reversed(s):
            cur = roman[i]
            if cur < prev:
                res -= cur
            else:
                res += cur
                prev = cur
        return res