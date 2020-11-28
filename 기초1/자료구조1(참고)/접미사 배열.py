import sys
scr = sys.stdin.readline()
li = []
for x in range(len(scr)):
    li.append(scr[x:-1])
li.sort()
li.remove('')
print('\n'.join(li))

        
   