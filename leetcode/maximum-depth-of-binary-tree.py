class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def __init__(self):
        self.ans = 0
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node, depth):
            if not node:
                return 
            if not node.left and not node.right:
                self.ans = max(self.ans, depth)
            helper(node.left, depth+1)
            helper(node.right, depth+1)
            
        helper(root, 1)
        return self.ans
#######################################################################3
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lft = self.maxDepth(root.left)+1
        rht = self.maxDepth(root.right)+1
        if rht>lft: return rht
        else: return lft
