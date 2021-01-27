c={'a':10,'b':1,'c':22}
tmp=list()
for k,v in c.items():
    tmp.append((v,k))

tmp=sorted(tmp,reverse=True)
print(tmp)

print(sorted([(v,k) for k,v in c.items()],reverse=True))
y=c.items()
print(y)
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])