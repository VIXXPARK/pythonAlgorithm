s="baa";p="aa"
s=list(s)
p=list(p)
size=len(p)
basket={}
default={}
answer=[]
for i in range(size):
    if basket.get(s[i],0)==0:
        basket[s[i]]=1
    else:
        basket[s[i]]+=1
        
    if default.get(p[i],0)==0:
        default[p[i]]=1
    else:
        default[p[i]]+=1
    
if(basket==default):
    answer.append(0)
for i in range(1,len(s)-size+1):
    if basket[s[i-1]]==1:
        del basket[s[i-1]]
    elif basket[s[i-1]]>1:
        basket[s[i-1]]-=1

    if basket.get(s[i+size-1],0)==0:
        basket[s[i+size-1]]=1
    else:
        basket[s[i+size-1]]+=1

    if basket==default:
        answer.append(i)

print(answer)