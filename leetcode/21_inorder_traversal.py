# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        
        def inorder(root,ans):
            if root is None:
                return
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        answer=[]
        inorder(root,answer)
        
        return answer
            
        