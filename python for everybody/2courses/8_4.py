fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    datas=(line.strip().split())
    for data in datas:
        lst.append(data)
lst.sort()
dx=set(lst)
dx=list(dx)
print(dx)