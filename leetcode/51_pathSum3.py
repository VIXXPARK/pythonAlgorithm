# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, s: int) -> int:
        return self.helper(root,s,[s])
    
    def helper(self,node,origin,targets):
        if node is None:
            return 0
        hit=0
        for t in targets:
            if not t-node.val: hit+=1
        targets = [t-node.val for t in targets] + [origin]
        return hit + self.helper(node.left,origin,targets)+ self.helper(node.right,origin,targets)
####################################################################################################
import collections
class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        
        hashmap = collections.defaultdict(int)
        result = [0]
        
        def helper(curr_sum, node, result):
            if not node:
                return 
            
            curr_sum += node.val
            
            if curr_sum == targetSum:
                result[0] += 1
            if curr_sum - targetSum in hashmap:
                result[0] += hashmap[curr_sum - targetSum]
                
            hashmap[curr_sum] += 1
            helper(curr_sum, node.left, result)
            helper(curr_sum, node.right, result)
            hashmap[curr_sum] -= 1
            
        helper(0, root, result)
        return result[0]