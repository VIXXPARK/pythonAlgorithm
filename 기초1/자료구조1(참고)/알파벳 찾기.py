import sys
script = sys.stdin.readline().rstrip()
script=list(script)
alpha=[-1]*26
for index,i in enumerate(script):
    if alpha[ord(i)-ord('a')]==-1:
        alpha[ord(i)-ord('a')]=index
alpha = list(map(str,alpha))
print(' '.join(alpha))