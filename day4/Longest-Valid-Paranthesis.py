class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        max_len = 0
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)

            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    max_len = max(max_len, i - stk[-1])

        return max_len