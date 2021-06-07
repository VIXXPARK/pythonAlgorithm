# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import defaultdict
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums=defaultdict(int)
        for value in lists:
            while value:
                nums[value.val]+=1
                value=value.next
        dummy=ListNode(0)
        prv=dummy
        for i in range(-10000,10001):
            if nums[i]!=0:
                for j in range(nums[i]):
                    prv.next=ListNode(i)
                    prv=prv.next
        return dummy.next

######################################################
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
#############################################################
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        new_head = ListNode()
        new_node = new_head
        
        nodes = []
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(nodes, (head.val, index, head))
        
        while nodes:
            val, index, node = heapq.heappop(nodes)
            new_node.next = node
            new_node = new_node.next

            node = node.next
            if node:
                heapq.heappush(nodes, (node.val, index, node))
        
        return new_head.next