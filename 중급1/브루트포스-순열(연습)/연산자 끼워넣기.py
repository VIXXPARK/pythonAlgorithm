import sys
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
sign=list(map(int,sys.stdin.readline().split()))
large=-sys.maxsize
small=sys.maxsize
def calc(left,right,sign):
    if sign==0:
        return left+right
    elif sign==1:
        return left-right
    elif sign==2:
        return left*right
    elif sign==3:
        if left*right>=0:
            return left//right
        else:
            return -(int(abs(left))//int(abs(right)))


def func(celi,aim,ans):
    global large,small
    if celi==aim-1:
        large=max(large,ans)
        small=min(small,ans)
        return
    
    for x in range(4):
        if  sign[x]!=0:

            sign[x]-=1
            k=calc(num[celi],num[celi+1],x)
            ans=k
            tmp=num[celi+1]
            num[celi+1]=ans

            func(celi+1,aim,ans)
            
            sign[x]=sign[x]+1
            num[celi+1]=tmp
            ans=0
            

func(0,N,0)
print(large)
print(small)

