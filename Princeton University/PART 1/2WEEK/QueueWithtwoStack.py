class queue:
    def __init__(self):
        self.stk1=[]
        self.stk2=[]
    
    def push(self,n):
        self.stk1.append(n)
    
    def pop(self):
        if len(self.stk2)!=0:
            return self.stk2.pop()
        else:
            while len(self.stk1):
                self.stk2.append(self.stk1.pop())
            if len(self.stk2)!=0:
                return self.stk2.pop() 
            else:
                return None

q=queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

    
