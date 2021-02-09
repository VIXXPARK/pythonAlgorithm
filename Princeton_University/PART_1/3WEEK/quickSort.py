def quick_sort(lst:list):
    def sort(low,high):
        if high<=low: ## 이부분에서 일정크기가 되면 삽입정렬을 돌리는 방법도 있다.
            return
        
        mid = partition(low,high)
        sort(low,mid-1)
        sort(mid,high)
    
    def partition(low,high):
        pivot= lst[(low+high)//2]
        while low<=high:
            while lst[low]<pivot:
                low+=1
            while lst[high]>pivot:
                high-=1
            if low<=high:
                lst[low],lst[high]=lst[high],lst[low]
                low,high=low+1,high-1
        return low
    return sort(0,len(lst)-1)

lst=[9,4,2,7,8,3,1]
quick_sort(lst)
print(lst)