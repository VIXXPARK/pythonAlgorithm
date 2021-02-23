def solution(key, lock):
    answer = True
    zerocount=0
    for i in lock:
        zerocount+=i.count(0)
    lx=len(lock)
    lk=len(key)
    block=[0 for _ in range(lx)]
    extLock=[]
    for i in range(3*lx):
        tmp=[]
        if lx<=i<lx*2:
            tmp=block+lock[i-lx]+block
        else:
            tmp=block+block+block
        extLock.append(tmp)
                    

    key2=list(map(list,zip(*key)))
    for k in key2:
        k.reverse()
        
    key3=[]
    for i in range(len(key)-1,-1,-1):
        x=key[i][:]
        x.reverse()
        key3.append(x)

    key4=list(map(list,zip(*key3)))
    for k in key4:
        k.reverse()

    for i in range(lx-lk+1,lx+lx):
        for j in range(lx-lk+1,lx+lx):
            flag=True
            cnt=0
            for y,val in enumerate(key):
                if lx<=i+y<lx*2:
                    for x,v in enumerate(val):
                        if lx<=j+x<lx*2:
                            if extLock[i][j]==1 and key[y][x]==1:
                                flag=False
                                break
                            elif extLock[i][j]==0 and key[y][x]==1:
                                cnt+=1
                if flag==False:
                    break
                if cnt==zerocount:
                    return True

            flag=True
            cnt=0
            for y,val in enumerate(key2):
                if lx<=i+y<lx*2:
                    for x,v in enumerate(val):
                        if lx<=j+x<lx*2:
                            if extLock[i][j]==1 and key2[y][x]==1:
                                flag=False
                                break
                            elif extLock[i][j]==0 and key2[y][x]==1:
                                cnt+=1
                if flag==False:
                    break
                if cnt==zerocount:
                    return True
            
            flag=True
            cnt=0
            for y,val in enumerate(key3):
                if lx<=i+y<lx*2:
                    for x,v in enumerate(val):
                        if lx<=j+x<lx*2:
                            if extLock[i][j]==1 and key3[y][x]==1:
                                flag=False
                                break
                            elif extLock[i][j]==0 and key3[y][x]==1:
                                cnt+=1
                if flag==False:
                    break
                if cnt==zerocount:
                    return True
            
            flag=True
            cnt=0
            for y,val in enumerate(key4):
                if lx<=i+y<lx*2:
                    for x,v in enumerate(val):
                        if lx<=j+x<lx*2:
                            if extLock[i][j]==1 and key4[y][x]==1:
                                flag=False
                                break
                            elif extLock[i][j]==0 and key4[y][x]==1:
                                cnt+=1
                if flag==False:
                    break
                if cnt==zerocount:
                    return True
    
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
