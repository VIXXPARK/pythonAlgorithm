import sys
a,b,c,d = map(str,sys.stdin.readline().split())
a+=b
c+=d
print(int(a)+int(c))