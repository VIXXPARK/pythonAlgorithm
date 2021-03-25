dic={}
cur=0
strs = ["eat","tea","tan","ate","nat","bat"]
for s in strs:
    if dic.get(''.join(sorted(s)),0)!=0:
        dic[''.join(sorted(s))].append(s)
    else:
        dic[''.join(sorted(s))]=[s]
dic=sorted(dic.items(),key=lambda x:len(x))
ans=[]
for i in range(len(dic)-1,-1,-1):
    ans.append(dic[i][1])

print(ans)