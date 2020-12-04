import sys
li = []
ans=0
for _ in range(9):
    li.append(int(input()))
    ans+=li[-1]
li.sort()
for i in range(8):
    for j in range(i+1,9):
        if ans-li[i]-li[j]==100:
            li[i]=0
            li[j]=0
            li.remove(0)
            li.remove(0)
            for i in li:
                print(i)
            exit()
       
