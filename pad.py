import random,collections,time
a=[]
b=[]
for i in range(1000000):
    x,y=random.randint(-10,30),random.randint(-10,30)
    q,w=random.randint(-10,30),random.randint(-10,30)
    a.append([x,y])
    b.append([q,w])
start=time.time()
def deciToStr(lst:list):
    ans=[]
    for val in lst:
        val=''.join(list(map(str,val)))
        ans.append(val)
    return ans

a=deciToStr(a) #n
b=deciToStr(b) #n
a=set(a) #n
b=set(b) #n
len(a)-len(a-b)
times=time.time()-start
print(times)
