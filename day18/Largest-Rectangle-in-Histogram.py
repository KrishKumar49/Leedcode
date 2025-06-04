class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
            
        def smallestNextElement(heights):
            stack = [-1]

            ans = [0] * n
            for i in range(n-1, -1, -1):
                cur = heights[i]
                while stack[-1] != -1 and heights[stack[-1]] >= cur:
                    stack.pop()

                ans[i] = stack[-1]
                stack.append(i)
            
            return ans


        def smallestPrevElement(heights):
            stack = [-1]

            ans = [0] * n
            for i in range(n):
                cur = heights[i]
                while stack[-1] != -1 and heights[stack[-1]] >= cur:
                    stack.pop()

                ans[i] = stack[-1]
                stack.append(i)

            return ans



        next = smallestNextElement(heights)
        prev = smallestPrevElement(heights)

        area = float('-inf')
        for i in range(n):
            l = heights[i]
            
            if next[i] == -1:
                next[i] = n

            b = next[i] - prev[i] - 1

            newArea = l * b
            
            area = max(area, newArea)

        return area



        