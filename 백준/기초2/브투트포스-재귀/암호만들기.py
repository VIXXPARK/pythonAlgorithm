import sys
L,C=map(int,sys.stdin.readline().split())
li=list(sys.stdin.readline().rstrip().split())
li.sort()
ans=[]
passing = [False]*C
consonant=0
vowel=0
def check(x):
    global consonant
    global vowel
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        consonant+=1
    else:
        vowel+=1
def backVal(x):
    global consonant
    global vowel
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        consonant-=1
    else:
        vowel-=1
def func(ans,celi,N):
    global li
    if celi==N:
        if consonant>=1 and vowel>=2:
            print(''.join(ans))
            return
        return
    for i in range(len(li)):
        if not ans:
            passing[i]=True
            check(li[i])
            ans.append(li[i])
            func(ans,celi+1,N)
            ans.pop()
            backVal(li[i])
            passing[i]=False
        elif not passing[i] and ord(ans[-1])<ord(li[i]):
            passing[i]=True
            check(li[i])
            ans.append(li[i])
            func(ans,celi+1,N)
            ans.pop()
            backVal(li[i])
            passing[i]=False  

func(ans,0,L)
