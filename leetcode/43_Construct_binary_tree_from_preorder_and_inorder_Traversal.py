# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.root=TreeNode()
    
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        cur=self.root
        def build(cur,preorder,inorder):
            try:
                cur.val=preorder[0]
                left=1
                right=inorder.index(preorder[0])+1
                if left<len(preorder):
                    if left!=right:
                        cur.left=TreeNode(preorder[left])
                        build(cur.left,preorder[left:right],inorder[left-1:right])
                if right<len(preorder):
                    cur.right=TreeNode(preorder[right])
                    build(cur.right,preorder[right:],inorder[right:])       
            except:
                return
        build(cur,preorder,inorder)
        return self.root
    

##########################################################################################

def buildTree(self, preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = self.buildTree(preorder, inorder[0:ind])
        root.right = self.buildTree(preorder, inorder[ind+1:])
        return root
        
        
        
                
            