from collections import deque
f=[1,2,3,4,5]
s=[2,1,2,3,2,4,5]
t=[3,3,1,1,2,2,4,4,5,5]
answers=[1,3,2,4,2]
answer=[0,0,0]
df=deque()
ds=deque()
dt=deque()
for fval in f:
    df.append(fval)
for sval in s:
    ds.append(sval)
for tval in t:
    dt.append(tval)
for val in answers:
    pf=df.popleft()
    ps=ds.popleft()
    pt=dt.popleft()
    if pf==val:
        answer[0]+=1
    if ps==val:
        answer[1]+=1
    if pt==val:
        answer[2]+=1
    df.append(pf)
    ds.append(ps)
    dt.append(pt)
maxVal=max(answer)
fin=[]
for check in range(len(answer)):
    if answer[check]==maxVal:
        fin.append(check+1)
print(fin)

#####################################
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
