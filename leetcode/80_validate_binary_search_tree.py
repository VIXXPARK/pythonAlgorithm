# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack=[]
        self.check=True
    def isValidBST(self, root: TreeNode) -> bool:
        self.helper(root)
        return True if self.check else False
    def helper(self,node):
        if node is None:
            return
        if node.left:
            self.helper(node.left)
        if self.stack and self.stack[-1]>=node.val:
            self.check=False
            node.left=None;node.right=None
        self.stack.append(node.val)
        if node.right:
            self.helper(node.right)