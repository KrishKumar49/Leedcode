class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        sol = []

        def backtrack(i):
            if i == len(digits):
                result.append(''.join(sol))
                return

            for l in phone[digits[i]]:
                sol.append(l)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return result