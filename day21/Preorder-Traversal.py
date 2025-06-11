class Solution:
    def preorderTraversal(sself, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def preoder(root):
            if root is None:
                return
            
            answer.append(root.val)
            preoder(root.left)
            preoder(root.right)
        
        preoder(root)
        return answer