class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits.reverse()

        digits[0] += 1
        for i in range(n):
            if digits[i] == 10:
                digits[i] = 0
                if i + 1 == n:
                    digits.append(1)
                else:
                    digits[i+1] = digits[i+1] + 1
            else:
                break

        digits.reverse()
        return digits
            
