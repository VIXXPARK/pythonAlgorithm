import sys
stk = []
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if(cmd[0]=='push'):
        stk.append(int(cmd[1]))
    elif(cmd[0]=='top'):
        print(stk[-1]) if len(stk)>=1 else print(-1)
    elif(cmd[0]=='size'):
        print(len(stk))
    elif(cmd[0]=='empty'):
        print(1)if len(stk)==0 else print(0)
    elif(cmd[0]=='pop'):
        print(stk.pop())if len(stk)>=1 else print(-1)