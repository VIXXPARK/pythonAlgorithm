import sys
N= int(sys.stdin.readline())
sign = list(sys.stdin.readline().split())
ans=[]

passing = [False]*(10)
li=[]
def func(ans,celi,aim,inequal):
    global sign,li
    if celi==aim:
        li.append(list(ans))
        return
    for i in range(10):
        if not ans:
            passing[i]=True
            ans.append(i)
            func(ans,celi+1,aim,inequal)
            passing[i]=False
            ans.pop()
        else:
            if not passing[i]:
                if sign[inequal]=='<':
                    if ans[-1]<i:
                        passing[i]=True
                        ans.append(i)
                        func(ans,celi+1,aim,inequal+1)
                        passing[i]=False
                        ans.pop()
                else:
                    if ans[-1]>i:
                        passing[i]=True
                        ans.append(i)
                        func(ans,celi+1,aim,inequal+1)
                        passing[i]=False
                        ans.pop()
func(ans,0,N+1,0)
for i in li[-1]:
    print(''.join(str(i)),end='')
print()
for i in li[0]:
    print(''.join(str(i)),end='')

