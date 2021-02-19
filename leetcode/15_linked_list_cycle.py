# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic={}
        while True:
            if head is None:
                return False
            if not dic.get(head,0):
                dic[head]=1
            else:
                return True
            head=head.next            