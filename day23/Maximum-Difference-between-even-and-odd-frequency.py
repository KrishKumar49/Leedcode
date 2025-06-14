class Solution:
    def MaximumDifference(self, s: str)-> int:
        counter = {}
        
        for char in s: 
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
                
        max_odd = 0
        min_even = float('inf')
        
        for val in counter.values():
            if val % 2 == 0:
                min_even = min(min_even, val)
            else:
                max_odd = max(max_odd, val)
        
        return max_odd - min_even