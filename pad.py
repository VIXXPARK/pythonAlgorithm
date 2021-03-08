nums=[1,2,3]
result=[[]]
for num in nums:
    result+=[i+[num] for i in result]
print(result)

