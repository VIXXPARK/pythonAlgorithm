# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        def find_max(node):
            if not node: return 0
            left, right = find_max(node.left), find_max(node.right)
            v = max(node.val, node.val + max(left, right))
            self.ans.add(left + node.val + right)
            self.ans.add(node.val)
            self.ans.add(v)
            return v
        self.ans = set()
        find_max(root)
        return max(self.ans)
######################################################################
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def dfs(root):
            if not root: return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            self.res = max(self.res,root.val+left+right)
            return max(left,right)+root.val
        dfs(root)
        return self.res