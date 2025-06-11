# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def postOrder(root):
            if root is None:
                return
            
            postOrder(root.left)
            postOrder(root.right)
            answer.append(root.val)

        postOrder(root)
        return answer