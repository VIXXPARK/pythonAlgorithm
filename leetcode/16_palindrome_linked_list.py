# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        if not head or not head.next:
            return True
        
        size = 0
        curr = head
        
        while curr:
            size += 1
            curr  = curr.next
                
        prev = None
        curr = head
        
        i = 0
        while i != size//2:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            i += 1
        first_half_start = prev
        second_half_start = curr
        
        if size%2 !=0:
            t = second_half_start.next
            h = first_half_start
        else:
            t = second_half_start
            h = first_half_start
        
        while t and h:
            if t.val != h.val : return False
            t = t.next
            h = h.next
        return True

#######################################################
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        if len(lst)%2:
            a=lst[:len(lst)//2]
            b=lst[len(lst)//2+1:]
            b.reverse()
            if a==b:
                return True
            else:
                return False
        else:
            a=lst[:len(lst)//2]
            b=lst[len(lst)//2:]
            b.reverse()
            if a==b:
                return True
            else:
                return False