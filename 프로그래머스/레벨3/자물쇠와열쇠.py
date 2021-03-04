def route(i,j,lock,ans,length,keylen,answer):
    flag=True
    cnt=0
    keyX=0
    for x in range(i,i+length):
        keyY=0
        for y in range(j,j+length):
            if 0<=x<length and 0<=y<length and (0<=keyX<keylen and 0<=keyY<keylen):
                if lock[x][y]==1 and ans[keyX][keyY]==1:
                    flag=False
                    break
                elif lock[x][y]==0 and ans[keyX][keyY]==1:
                    cnt+=1
            keyY+=1
        if not flag:
            return False
        keyX+=1
    if cnt==answer:
        return True
    return False

def solution(key, lock):
    answer = 0
    length=len(key)
    lockLen=len(lock)
    rotate90 = list(map(list,zip(*key)))
    for i in range(length):
        rotate90[i].reverse()
    rotate180 = list(map(list,zip(*rotate90)))
    for i in range(length):
        rotate180[i].reverse()
    rotate270 = list(map(list,zip(*rotate180)))
    for i in range(length):
        rotate270[i].reverse()
    for i in range(lockLen):
        answer+=lock[i].count(0)
    for ans in [key,rotate90,rotate180,rotate270]:
        for i in range(-length+1,lockLen):
            for j in range(-length+1,lockLen):
                if route(i,j,lock,ans,lockLen,length,answer):
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


###########################################################################

def solution2(key, lock):
    N = len(lock)
    v, vac = vacant(lock)
    if not vac: return True
    vac = vac[0]
    find = False
    for key in rotate(key):
        for i in range(len(key)):
            cnt = 0
            rr, cc = vac[0]-key[i][0], vac[1]-key[i][1]
            print(rr, cc)
            for j in range(i, len(key)):
                r, c = key[j]
                r, c = r+rr, c+cc
                if not (0 <= r < N and 0 <= c < N): continue
                if lock[r][c] == 1: break
                cnt += 1
            if cnt == v:
                find = True
                break
        if find: break
    if find: return True
    return False


def vacant(lock):
    N = len(lock)
    vac = []
    v = 0
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 0:
                vac.append((r, c))
                v += 1
    return v, vac


def rotate(key):
    M = len(key)
    key1 = [(r, c) for r in range(M) for c in range(M) if key[r][c] == 1]
    key2 = [(M-r-1, c) for c, r in key1]
    key3 = [(r, M-c-1) for c, r in key1]
    key4 = [(M-r-1, M-c-1) for r, c in key1]

    key1 = quick_sort(key1)
    key2 = quick_sort(key2)
    key3 = quick_sort(key3)
    key4 = quick_sort(key4)
    print(key1, key2, key3, key4)

    return key1, key2, key3, key4


def quick_sort(arr):
    if not arr: return []
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [pivot], []

    for pos in arr:
        if pos[0] < pivot[0]:
            lesser.append(pos)
        elif pos[0] > pivot[0]:
            greater.append(pos)
        else:
            if pos[1] < pivot[1]:
                lesser.append(pos)
            elif pos[1] > pivot[1]:
                greater.append(pos)

    return quick_sort(lesser) + equal + quick_sort(greater)