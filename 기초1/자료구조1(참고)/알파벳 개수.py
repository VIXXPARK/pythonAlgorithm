import sys
script = sys.stdin.readline().rstrip()
alpha=[0]*26
for i in script:
    alpha[ord(i)-ord('a')]+=1
alpha = list(map(str,alpha))
print(' '.join(alpha))