# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lst=[]
        while head!=None:
            lst.append(head.val)
            head=head.next
        lst.reverse()
        if len(lst)!=0:
            tail=ListNode(lst[0])
            target=tail
            for i in range(1,len(lst)):
                val=ListNode(lst[i])
                target.next=val
                target=target.next
        else:
            return None
        return tail
######################################################
class Solution2:
    def reverseList(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)