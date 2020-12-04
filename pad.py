start = 1
startCandy=ar[k][j]
for t in range(1,N):
    if startCandy==ar[t][j]:
        start+=1
    else:
        start=1
        startCandy=ar[t][j]