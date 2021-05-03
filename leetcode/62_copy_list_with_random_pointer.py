class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None     
        # build mapping of original node to it's copy
        current = head
        mapping = {}
        while current:
            copy = Node(current.val)
            mapping[id(current)] = copy
            current = current.next
            
        # now that we have the complete mapping, we can use it to
        # construct the linked list copy
        current = head
        while current:
            
            # we have all the copy nodes but they aren't connected i.e. the next
            # & random all point to None. let's connect them here. it's easy
            # since we have a complete node-to-copy mapping
            if current.next:
                mapping[id(current)].next = mapping[id(current.next)]
            if current.random:
                mapping[id(current)].random = mapping[id(current.random)]
            current = current.next
            
        # return the head of the linked list copy
        return mapping[id(head)]