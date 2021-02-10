# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 !=None and l2!=None:
            if l1.val>l2.val:
                l3=ListNode(l2.val)
                l2=l2.next
            else:
                l3=ListNode(l1.val)
                l1=l1.next
        elif l1 is None and l2 !=None:
            l3=ListNode(l2.val)
            l2=l2.next
        elif l1 != None and l2 is None:
            l3=ListNode(l1.val)
            l1=l1.next
        else:
            l3=None
        cur=l3
        while not (l1 is None) and not (l2 is None):
            if l1 != None and l2 != None and l1.val>l2.val:
                val=ListNode(l2.val)
                cur.next=val
                cur=cur.next
                l2=l2.next
            elif l1 != None and l2 != None:
                val=ListNode(l1.val)
                cur.next=val
                cur=cur.next
                l1=l1.next
        if l1 is None:
            while l2 != None:
                val=ListNode(l2.val)
                cur.next=val
                cur=cur.next
                l2=l2.next
        else:
            while l1 != None:
                val=ListNode(l1.val)
                cur.next=val
                cur=cur.next
                l1=l1.next
        return l3


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tmp = dummy

        while(l1 or l2):
            if l1 and l2:
                if l1.val < l2.val:
                    tmp.next = l1
                    l1 = l1.next
                    tmp = tmp.next
                else:
                    tmp.next = l2
                    l2 = l2.next
                    tmp = tmp.next
            elif l1:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next

            elif l2:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next

        return dummy.next