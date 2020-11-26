import sys
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().strip()
    stk =0
    flag=0
    for x in line:
        if x=='(':
            stk+=1
        else:
            if stk>=1:
                stk-=1
            else:
                flag=1
                break
    if flag==0 and stk==0:
        print("YES")
    else:
        print("NO")
