class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        sol = []

        def backtrack(i, summ):
            
            if summ == target:
                result.append(sol[:])
                return 

            if summ > target or i == len(candidates):
                return 
            
            backtrack(i+1, summ)

            sol.append(candidates[i])
            backtrack(i, summ + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return result