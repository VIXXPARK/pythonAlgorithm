import sys
val=[False]*(21)
for _ in range(int(sys.stdin.readline().rstrip())):
    cmd=sys.stdin.readline().rstrip().split()
    if cmd[0]=='add':
        val[int(cmd[1])]=True
    elif cmd[0]=='check':
        print(1) if val[int(cmd[1])] else print(0)
    elif cmd[0]=='toggle':
        if val[int(cmd[1])]:
            val[int(cmd[1])]=False
        else:
            val[int(cmd[1])]=True
    elif cmd[0]=='all':
        val=[True]*21
    elif cmd[0]=='remove':
        val[int(cmd[1])]=False
    else:
        val=[False]*21