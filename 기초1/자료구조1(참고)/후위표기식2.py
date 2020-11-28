import sys
def calc(left,right,mid):
    if mid=='+':
        return left+right
    elif mid=='*':
        return left*right
    elif mid=='-':
        return left-right
    elif mid=='/':
        return left/right


num=int(sys.stdin.readline().rstrip())
script=sys.stdin.readline().rstrip()
li=[]
stk=[]
val=[]
for x in script:
        li.append(x)
li.reverse()
for _ in range(num):
    val.append(int(sys.stdin.readline().rstrip()))
while(len(li)):
    if li[-1]>='A' and li[-1]<='Z':
       stk.append(val[ord(li.pop())-ord('A')])
    else:
        right = stk.pop()
        left=stk.pop()
        stk.append(calc(left,right,li.pop()))

print('%.2f' % stk[-1])