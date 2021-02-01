from functools import reduce
power = lambda x:x**2
print(power(2))
a=[1,2,3,4]
b=[4,3,2,1]
c=reduce(lambda x,y:y-x,a)
print(c)
foo=[3,4,6,7,8,12,15,16,27]
bar = list(filter(lambda x:x%3==0,foo))
print(bar)