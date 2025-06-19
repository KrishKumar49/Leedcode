from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row):
            left = 0
            right = col - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if matrix[r][mid] == target:
                    return True
                elif matrix[r][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
    
    
    
class SolutionBinarySearch:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        
        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col
            mid_val = matrix[r][c]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    solution = Solution()
    print(solution.searchMatrix(matrix, target))
    
    target = 13
    print(solution.searchMatrix(matrix, target))
    solution_binary_search = SolutionBinarySearch()
    print(solution_binary_search.searchMatrix(matrix, target))
