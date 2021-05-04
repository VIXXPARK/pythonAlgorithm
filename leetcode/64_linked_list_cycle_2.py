# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode: ##id로 키값으로 설정하면 속도가 더 빨라진다!!
        cur=head
        node={}
        count=0
        while cur:
            if node.get(id(cur),-1)==-1:
                node[id(cur)]=count
            else:
                return cur
            count+=1
            cur=cur.next
        
        return None
            
            