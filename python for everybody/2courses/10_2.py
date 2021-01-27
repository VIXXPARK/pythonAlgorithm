name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic={}
for line in handle:
    lst=line.split()
    if not line.startswith("From "): continue
    if len(lst)<5: continue
    val=lst[5].split(':')
    dic[val[0]]=dic.get(val[0],0)+1
for k,v in sorted(dic.items()):
    print(k,v)
