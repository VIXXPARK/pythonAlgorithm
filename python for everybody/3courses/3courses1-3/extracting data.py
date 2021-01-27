import re
data = open('actual_data.txt')
sum=0
for line in data:
    lst=re.findall('[0-9]+',line.strip())
    for val in lst:
        sum+=int(val)
print(sum)