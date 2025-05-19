# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(root):
            if root == None:
                return

            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result
    
    
# # -------------------------------------------
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right
