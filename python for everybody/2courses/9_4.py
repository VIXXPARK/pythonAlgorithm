name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic={}
for line in handle:
    lst=line.split()
    if not line.startswith("From:"): continue
    if len(lst)!=2: continue
    dic[lst[1]]=dic.get(lst[1],0)+1
bigCount=None
bigName=None
for k,v in dic.items():
    if bigCount is None:
        bigCount=v
        bigName=k
    else:
        if bigCount<v:
            bigCount=v
            bigName=k
print(bigName,bigCount)
