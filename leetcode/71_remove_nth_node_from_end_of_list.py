# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur=head;node=[]
        while cur:
            node.append(cur)
            cur=cur.next
        if n==len(node):
            return head.next
        try:
            n=-1*n
            out=node[n-1]
            out.next=out.next.next
            return head
        except:
            return None

####################################################################################
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head