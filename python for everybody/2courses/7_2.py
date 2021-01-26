# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
val=0
cnt=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    start=line.find(':')
    num=line[start+1:]
    val+=float(num)
    cnt+=1
print("Average spam confidence:",val/cnt)
