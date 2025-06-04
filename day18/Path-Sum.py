# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currSum):
            if root is None:
                return False

            if root.left is None and root.right is None:
                return (currSum + root.val) == targetSum
            
            left_found = dfs(root.left, currSum + root.val)
            if left_found:
                return True

            right_found = dfs(root.right, currSum + root.val)
            if right_found:
                return True

            return False

        return dfs(root, 0)