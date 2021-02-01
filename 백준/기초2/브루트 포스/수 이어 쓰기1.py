N=int(input())
ans=0
start=1
num=1
wall=10-1
while True:
    if wall<N:
        ans+=(wall-start+1)*num
        wall=start*100-1
        start*=10
        num+=1
    else:
        ans+=(N-start+1)*num
        break  
print(ans)