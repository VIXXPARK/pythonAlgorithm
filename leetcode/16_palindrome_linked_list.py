# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(self, head):
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next #두배로 돌리면 slow는 그의 절반만 가기때문에
        rev, rev.next, slow = slow, rev, slow.next # 뒤집기 코드
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev

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