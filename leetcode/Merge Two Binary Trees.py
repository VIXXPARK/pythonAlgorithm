class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def order(t1,t2):
    t1.val=t1.val+t2.val
    if t1.left!=None and t2.left!=None:
        order(t1.left,t2.left)
    elif t1.left==None and t2.left!=None:
        t1.left=TreeNode()
        order(t1.left,t2.left)
    elif t1.left!=None and t2.left==None:
        t2.left=TreeNode()
        order(t1.left,t2.left)
    if t1.right!=None and t2.right!=None:
        order(t1.right,t2.right)
    elif t1.right==None and t2.right!=None:
        t1.right=TreeNode()
        order(t1.right,t2.right)
    elif t1.right!=None and t2.right==None:
        t2.right=TreeNode()
        order(t1.right,t2.right)

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
        flag=0
        t3=t1
        if t1==None:
            flag+=1
            t1=TreeNode()
        if t2==None:
            flag+=1
            t2=TreeNode()
        order(t1,t2)
        if flag!=2:
            return t1
        else: return t3

# ################################################################
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None: 
            return t2
        if t2 is None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

####################################################################
class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        Initial thoughts: iterate both trees in depth first order
        When you have a node mismatch just add the non-null node directly into the tree and stop traversing
        """
        if (t1 is None or t1.val is None) and (t2 is None or t2.val is None):
            return None
        if (t1 is None or t1.val is None):
            return t2
        if (t2 is None or t2.val is None):
            return t1
        
        n = TreeNode(val=t1.val+t2.val)
        n.left = self.mergeTrees(t1.left, t2.left)
        n.right = self.mergeTrees(t1.right, t2.right)
        return n