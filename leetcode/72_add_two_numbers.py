# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left=[];right=[]
        while l1:
            left.append(l1.val)
            l1=l1.next
        while l2:
            right.append(l2.val)
            l2=l2.next
        if len(left)>=len(right):
            pass
        else:
            left,right=right,left
        
        for i in range(len(left)):
            if i<len(right):
                left[i]+=right[i]
            if left[i]>=10:
                if i+1<len(left):
                    left[i+1]+=left[i]//10
                else:
                    left.append(left[i]//10)
                left[i]-=(left[i]//10)*10        
        ret=ListNode(0)
        cur=ret
        for i in left:
            val=ListNode(i)
            cur.next=val
            cur=cur.next
        return ret.next

##################################################################################

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        carry = 0
        
        while l1 or l2 or carry:
            x = (l1.val if l1 else 0)
            y = (l2.val if l2 else 0)
            total = x+y+carry
            carry = int(total//10)
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = (l1.next if l1 else l1)
            l2 = (l2.next if l2 else l2)
            
        return head.next