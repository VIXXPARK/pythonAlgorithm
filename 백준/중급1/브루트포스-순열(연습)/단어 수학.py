import sys
N = int(sys.stdin.readline().rstrip())
words=[sys.stdin.readline().rstrip()  for _ in range(N)]
alphabet=[0]*26
for word in words:
    i=0
    while word: 
        num=ord(word[-1])-ord('A')
        alphabet[num]+=pow(10,i)
        i+=1
        word=word[:-1]
alphabet.sort(reverse=True)
ans=0
idx=0
for i in range(9,-1,-1):
    ans+=alphabet[idx]*i
    idx+=1
print(ans)
