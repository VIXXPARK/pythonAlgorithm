import sys
from collections import deque
total = int(sys.stdin.readline().strip())
d = deque()
for _ in range(total):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0]=='push_back': d.append(cmd[1])
    elif cmd[0]=='push_front': d.appendleft(cmd[1])
    elif cmd[0]=='front':
        print(d[0]) if len(d)>0 else print(-1)
    elif cmd[0]=='back':
        print(d[-1]) if len(d)>0 else print(-1)
    elif cmd[0]=='size':
        print(len(d))
    elif cmd[0]=='empty':
        print(1) if len(d)==0 else print(0)
    elif cmd[0]=='pop_front':
        print(d.popleft()) if len(d)>0 else print(-1)
    elif cmd[0]=='pop_back':
        print(d.pop()) if len(d)>0 else print(-1)
