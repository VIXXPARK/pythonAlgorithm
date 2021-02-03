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
    def reverseList2(self, head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            cur, prev = head, None
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            return prev


class Solution2(object):
    def reverseList(self, head, prev=None):
        if not head:
          return prev
  
        curr, head.next = head.next, prev
        return self.reverseList(curr, head)