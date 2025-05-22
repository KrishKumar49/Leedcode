class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        sol = []
        summ = 0
        nex_index = [len(candidates)] * len(candidates)

        def backtrack(i, summ):
            if summ == target:
                result.append(sol[:])
                return

            if summ > target or i == len(candidates):
                return

            # take 
            sol.append(candidates[i])
            backtrack(i+1, summ + candidates[i])
            sol.pop()

            # not take
            for m in range(len(candidates)):
                for n in range(m + 1, len(candidates)):
                    if candidates[m] != candidates[n]:
                        nex_index[m] = n
                        break

            backtrack(nex_index[i],summ) 



        backtrack(0, 0)
        return result