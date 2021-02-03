import collections,time,random
def binary_search(lst:list,startNum:int,target:int):
    start=startNum+1
    end=len(lst)-1
    while start <= end:
        mid= start + (end-start)//2
        if lst[mid]>target:
            end=mid-1
        elif lst[mid]<target:
            start=mid+1
        else:
            return mid
    return -1

def three_sum(lst:list,target:int):
    answer=[]
    cnt=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if binary_search(lst,j,target-lst[i]-lst[j])==-1:
                continue
            else:
                answer.append([lst[i],lst[j],target-lst[i]-lst[j]])
                cnt+=1
    return cnt


def three_sum2(lst:list,target:int):
    cnt=0
    answer=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            for k in range(j+1,len(lst)):
                if lst[i]+lst[j]+lst[k]==target:
                    cnt+=1
                    answer.append([lst[i],lst[j],lst[k]])
    return cnt
def random_List(size):
    result=[]
    for _ in range(size):
        result.append(random.randint(-10000,10000))
    return result

lst=random_List(1000)
lst=list(set(lst))
lst.sort()
start= time.time()
fi=three_sum(lst,0)
print(fi)
second=time.time()-start
print("time :",second)
se=three_sum2(lst,0)
print(se)
print("time :",time.time()-start)