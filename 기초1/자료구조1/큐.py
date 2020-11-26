import sys
from collections import deque
d = deque()
for _ in range(int(sys.stdin.readline().strip())):
    cmd = sys.stdin.readline().strip().split()
    if(cmd[0]=='push'):
        d.append(int(cmd[1]))
    elif(cmd[0]=='front'):
        print(d[0]) if len(d)>=1 else print(-1)
    elif(cmd[0]=='back'):
        print(d[-1]) if len(d)>=1 else print(-1)
    elif(cmd[0]=='empty'):
        print(1) if len(d)==0 else print(0)
    elif(cmd[0]=='pop'):
        print(d.popleft()) if len(d)>0 else print(-1)
    elif(cmd[0]=='size'):
        print(len(d))
