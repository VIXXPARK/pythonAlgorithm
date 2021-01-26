fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count=0
for lines in fh:
    if not lines.startswith('From'): continue
    lst=lines.split()
    if lst[-1]!='2008':
        continue
    print(lst[1])
    count+=1
print("There were",count,"lines in the file with From as the first word")
    