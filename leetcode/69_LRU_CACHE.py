class LRUCache:                     ##내 솔루션
    from collections import deque
    def __init__(self, capacity: int):
        self.queue=deque()
        self.cache={}
        self.current=0
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if self.cache.get(key,-1)==-1:
            return -1
        else:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if self.current<self.capacity:
            if self.cache.get(key,-1)==-1:
                self.queue.appendleft(key)
                self.cache[key]=value
                self.current+=1
            else:
                self.queue.remove(key)
                self.queue.appendleft(key)
                self.cache[key]=value
        else:
            if self.cache.get(key,-1)==-1:
                loc=self.queue.pop()
                del self.cache[loc]
                self.queue.appendleft(key)
                self.cache[key]=value
            else:
                self.queue.remove(key)
                self.queue.appendleft(key)
                self.cache[key]=value
######################################################################
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Gotta keep this pair fresh, move to end of OrderedDict
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) # last=True, LIFO; last=False, FIFO. We want to remove in FIFO fashion. 
        else:
            self.cache.move_to_end(key) # Gotta keep this pair fresh, move to end of OrderedDict 

        self.cache[key] = value

##########################################################################################################################

class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict() # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()        
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else: 
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key,value)
            self.dic[key] = node
            self.insertIntoHead(node)
			
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertIntoHead(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node
    
    def removeFromTail(self):
        if len(self.dic) == 0: return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)