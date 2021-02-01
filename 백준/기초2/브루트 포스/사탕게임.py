import sys

N=int(input())
ar= [[0]*N for _ in range(N)]
for i in range(N):
    script= sys.stdin.readline().rstrip()
    for j in range(N):
        ar[i][j]=script[j]
ans=1        
for i in range(N):
    for j in range(N):
        if j!=N-1:
            if i!=N-1:
                ar[i][j],ar[i][j+1]=ar[i][j+1],ar[i][j]
                start=1
                startCandy=ar[0][j]
               
                for t in range(1,N):
                    if startCandy==ar[t][j]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[t][j]
                    ans=max(ans,start)
            
                start=1
                startCandy=ar[0][j+1]
               
                for t in range(1,N):
                    if startCandy==ar[t][j+1]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[t][j+1]
                    ans=max(ans,start)
                
                start=1
                startCandy=ar[i][0]
               
                for t in range(1,N):
                    if startCandy==ar[i][t]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[i][t]
                    ans=max(ans,start)

                ar[i][j],ar[i][j+1]=ar[i][j+1],ar[i][j]

                ar[i][j],ar[i+1][j]=ar[i+1][j],ar[i][j]

                start=1
                startCandy=ar[i][0]
               
                for t in range(1,N):
                    if startCandy==ar[i][t]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[i][t]
                    ans=max(ans,start)

                start=1
                startCandy=ar[i+1][0]
               
                for t in range(1,N):
                    if startCandy==ar[i+1][t]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[i+1][t]
                    ans=max(ans,start)

                ar[i][j],ar[i+1][j]=ar[i+1][j],ar[i][j]

            else:
                ar[i][j],ar[i][j+1]=ar[i][j+1],ar[i][j]

                start=1
                startCandy=ar[0][j]
               
                for t in range(1,N):
                    if startCandy==ar[t][j]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[t][j]
                    ans=max(ans,start)

                start=1
                startCandy=ar[0][j+1]
               
                for t in range(1,N):
                    if startCandy==ar[t][j+1]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[t][j+1]
                    ans=max(ans,start)


                ar[i][j],ar[i][j+1]=ar[i][j+1],ar[i][j]
        else:
            if i!=N-1:
                ar[i][j],ar[i+1][j]=ar[i+1][j],ar[i][j]

                start=1
                startCandy=ar[i][0]
               
                for t in range(1,N):
                    if startCandy==ar[i][t]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[i][t]
                    ans=max(ans,start)


                start=1
                startCandy=ar[i+1][0]
               
                for t in range(1,N):
                    if startCandy==ar[i+1][t]:
                        start+=1
                    else:
                        start=1
                        startCandy=ar[i+1][t]
                    ans=max(ans,start)

                ar[i][j],ar[i+1][j]=ar[i+1][j],ar[i][j]
print(ans)


