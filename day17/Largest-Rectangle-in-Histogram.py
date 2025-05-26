def largestRectangleArea(heights):
    n = len(heights)
    
    def nextSmallestElement(heights):
        stack = [-1]
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            cur = heights[i]
            
            while stack[-1] != -1 and heights[stack[-1]] >= cur:
                stack.pop()
                
            ans[i] = stack[-1]
            stack.append(i)
            
        return ans


    def prevSmallestElement(heights):
        stack = [-1]
        ans = [0] * n
        
        for i in range(n):
            cur = heights[i]
            
            while stack[-1] != -1 and heights[stack[-1]] >= cur:
                stack.pop()
                
            ans[i] = stack[-1]
            stack.append(i)
            
        return ans
    
    
    next = nextSmallestElement(heights)
    prev = prevSmallestElement(heights)
    
    area = float('-inf')
    
    for i in range(n):
        l = heights[i]
        
        if next[i] == -1:
            next[i] = n
        
        b = next[i] - prev[i] - 1
        
        newArea = l * b
        area = max(area, newArea)
        
    return area



if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))
    heights = [2,4]
    print(largestRectangleArea(heights))
    heights = [1,1]
    print(largestRectangleArea(heights))