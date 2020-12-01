val = input()
sum=0
left=0
for i in range(len(val)):
    if val[i]=='(':
        left+=1
    elif val[i]==')':
        left-=1
        if val[i-1]=='(':
            sum+=left
        else:
            sum+=1
print(sum)