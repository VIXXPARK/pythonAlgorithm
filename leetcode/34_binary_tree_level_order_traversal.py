# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        q = [root]
        
        res = []
        
        while q:
            size = len(q)
            currLevel = []
            
            for node in q:
                currLevel.append(node.val)
            
            res.append(currLevel)
            
            for _ in range(size):
                x = q.pop(0)
                if x.left!= None: q.append(x.left)
                if x.right!= None: q.append(x.right)
        
        
        return res