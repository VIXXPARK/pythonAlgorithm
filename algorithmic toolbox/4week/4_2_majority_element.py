import collections
sz=int(input())
lst=list(map(int,input().split()))
dic=collections.Counter(lst).most_common()
if dic[0][1]>len(lst)//2:
    print(1)
else:
    print(0)