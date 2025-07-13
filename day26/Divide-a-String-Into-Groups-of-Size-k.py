class Solution:
    def divideString(self, s: str, k: int, fill: str) -> int:
        rem = 0
        if len(s) % k != 0:
            rem = k - (len(s) % k)
            
        result = s + fill * rem
        
        ans = []
        for i in range(0, len(result), k):
            ans.append(result[i: i+ k])
            
        return ans
    
    
    
if __name__ == "__main__":
    s = "abcdefghi"
    k = 3
    fill = "x"
    solution = Solution()
    print(solution.divideString(s, k, fill))  # Output: ['abc', 'def', 'ghi']
    
    s = "abcdefghij"
    k = 3
    fill = "x"
    print(solution.divideString(s, k, fill))  # Output: ['abc', 'def', 'ghi', 'jxx']
    
    
    s = "umrcmcqqkchpwnudzdoqz"
    k = 74
    fill = "b"
    print(solution.divideString(s, k, fill))  # Output: ['umrcmcqqkchpwnudzdoqz']