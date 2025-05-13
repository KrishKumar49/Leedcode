class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):
                for k in range(j, len(p)):
                    if p[k] != '*':
                        memo[(i, j)] = False
                        return False
                memo[(i, j)] = True
                return True

            if p[j] == '?':
                result = dp(i + 1, j + 1)

            elif p[j] == '*':
                result = dp(i, j + 1) or dp(i + 1, j)

            elif s[i] == p[j]:
                result = dp(i + 1, j + 1)

            else:
                result = False

            memo[(i, j)] = result
            return result

        return dp(0, 0)
