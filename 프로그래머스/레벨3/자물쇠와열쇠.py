def solution(key, lock):
    answer = True
    zerocount=0

    for i in lock:
        zerocount+=i.count(0)

    if not zerocount:
        return True

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
                    
    key2=list(map(list,zip(*key))) #90도 회전
    for k in key2:
        k.reverse()
        
    key3=[]#180도 회전
    for i in range(len(key)-1,-1,-1):
        x=key[i][:]
        x.reverse()
        key3.append(x)

    key4=list(map(list,zip(*key3)))#270도 회전
    for k in key4:
        k.reverse()

    for ks in [key,key2,key3,key4]:
        for i in range(lx-lk,lx+lx+1):                                                   
            for j in range(lx-lk,lx+lx+1):
                flag=True
                cnt=0
                for y,val in enumerate(ks):
                    if lx<=i+y<lx*2:
                        for x,v in enumerate(val):
                            if lx<=j+x<lx*2:
                                if extLock[i+y][j+x]==1 and ks[y][x]==1:
                                    flag=False
                                    break
                                elif extLock[i+y][j+x]==0 and ks[y][x]==1:
                                    cnt+=1
                if cnt==zerocount and flag:
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))