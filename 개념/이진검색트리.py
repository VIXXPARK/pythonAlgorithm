class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None


class BST:

    def __init__(self):
        self.root=None
    
    def insert(self,item):
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            parent = current
            if item<current.item:
                current=current.left
                if current is None:
                    parent.left = new_node
                    break
            else:
                current = current.right
                if current is None:
                    parent.right = new_node
                    break
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.item,end=' ')
            self.inorder(node.right)
    
    def get_min(self,current):
        while current.left is not None:
            current=current.left
        return current
    
    def delete(self,item):
        self.root = self.delete_node(self.root,item)
    
    def delete_node(self,current,item):
        if current is None:
            return None
        
        if current.item>item:
            current.left = self.delete_node(current.left,item)
            return current
        elif current.item<item:
            current.right = self.delete_node(current.right,item)
            return current
        else:
            if (current.left is None) and (current.right is None):
                return None
            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            else:
                min_node = self.get_min(current.right)
                current.item = min_node.item
                current.right = self.delete_node(current.right,min_node.item)
                return current


        