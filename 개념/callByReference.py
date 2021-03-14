def swap(a,b):
    a[0],b[0]=b[0],a[0] # python은 call by reference는 공식적으로는 불가능하기 때문에 list,dic,set 과 같은 mutable object로 넘겨서 해결해야 한다.
    print("In function",a,b)

a=[2];b=[6]
print(a,b)
swap(a,b)
print(a,b)