# class Solution:
#     def permutation(self, lst: List[int]):
#         if len(lst) == 0:
#             return []

#         if len(lst) == 1:
#             return [lst]

#         result = []
#         for i in range(len(lst)):
#             m = lst[i]
#             remlst = lst[:i] + lst[i+1:]

#             for p in self.permutation(remlst):
#                 result.append([m] + p)
                
#         return result


#     def getPermutation(self, n: int, k: int) -> str:
#         lst = [i for i in range(1, n+1)]
#         all_perm = self.permutation(lst)
#         all_perm.sort()
#         kth_perm = all_perm[k-1]
#         ans = "".join(map(str,  kth_perm))

#         return ans



# -------------------------------------------



# class Solution:
#     def getPermutation(self, n: int, k: int) -> str:
#         result = []
#         sol = []
#         used = [False] * (n + 1)

#         def backtrack():
#             if len(sol) == n:
#                 result.append("".join(map(str, sol)))
#                 return

#             for i in range(1, n + 1):
#                 if not used[i]:
#                     used[i] = True
#                     sol.append(i)
#                     backtrack()
#                     sol.pop()
#                     used[i] = False

#         backtrack()
#         return result[k - 1] 




# -------------------------------------------




class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]

        result = []
        factorial = math.factorial(n)
        index = k - 1

        while nums:
            factorial = factorial // len(nums)
            pos = index // factorial
            number = nums.pop(pos)
            result.append(number)
            index = index % factorial

        return "".join(map(str, result))