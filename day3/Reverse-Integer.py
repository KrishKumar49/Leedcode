class Solution:

    def is_32bit(self, n: int) -> bool:
        return -2**31 <= n <= 2**31 - 1


    def reverse(self, x: int) -> int:
        if x < 0 :
            x = str(abs(x))
            i = -int(x[::-1])

        else:
            i = int(str(x)[::-1])

        if not self.is_32bit(i) :
            return 0
        return i
        