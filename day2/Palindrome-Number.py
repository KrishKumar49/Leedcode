class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = []
        if x < 0:
            return False
        while x != 0:
            digit = x % 10
            arr.append(digit)
            x = x // 10
        arr.reverse()
        length = len(arr)
        if length == 0:
            return True
        
        if length == 1:
            return True
        
        left = 0
        right = length - 1

        while left < right:
            if arr[left] != arr[right] :
                return False
            else:
                left = left + 1
                right = right - 1
        return True
        

        