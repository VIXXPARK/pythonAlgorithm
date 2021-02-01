import sys
numList = []
ans = []
count=1
isTrue = True
for i in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    while count<=num:
        numList.append(count)
        ans.append('+')
        count+=1
    if numList[-1]==num:
        numList.pop()
        ans.append('-')
    else:
        isTrue=False

if isTrue==False:
    print('NO')
else:
    for x in ans:
        print(x)
