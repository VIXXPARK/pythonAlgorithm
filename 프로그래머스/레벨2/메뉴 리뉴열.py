import re,bisect
info =["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

query=["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]
def score(info,query):
    return int(info)>=int(query)

infos=[]
querys=[]
lang={'java':0,'python':1,'cpp':2,'-':3}
job={'backend':0,'frontend':1,'-':2}
stage={'junior':0,'senior':1,'-':2}
soul = {'pizza':0,'chicken':1,'-':2}
result=[[[[ [] for soul in range(3)] for stage in range(3)]for job in range(3)]for lang in range(4)]
vs=[0 for _ in range(len(query))]              
for x in info:
    xx=(x.split())
    result[lang[xx[0]]][job[xx[1]]][stage[xx[2]]][soul[xx[3]]].append(int(xx[4]))
    result[lang['-']][job['-']][stage['-']][soul['-']].append(int(xx[4]))
    result[lang['-']][job['-']][stage['-']][soul[xx[3]]].append(int(xx[4]))
    result[lang['-']][job['-']][stage[xx[2]]][soul['-']].append(int(xx[4]))
    result[lang['-']][job[xx[1]]][stage['-']][soul['-']].append(int(xx[4]))
    result[lang[xx[0]]][job['-']][stage['-']][soul['-']].append(int(xx[4]))
    result[lang[xx[0]]][job[xx[1]]][stage['-']][soul['-']].append(int(xx[4]))
    result[lang[xx[0]]][job['-']][stage[xx[2]]][soul['-']].append(int(xx[4]))
    result[lang[xx[0]]][job['-']][stage['-']][soul[xx[3]]].append(int(xx[4]))
    result[lang['-']][job[xx[1]]][stage[xx[2]]][soul['-']].append(int(xx[4]))
    result[lang['-']][job[xx[1]]][stage['-']][soul[xx[3]]].append(int(xx[4]))
    result[lang['-']][job['-']][stage[xx[2]]][soul[xx[3]]].append(int(xx[4]))
    result[lang['-']][job[xx[1]]][stage[xx[2]]][soul[xx[3]]].append(int(xx[4]))
    result[lang[xx[0]]][job['-']][stage[xx[2]]][soul[xx[3]]].append(int(xx[4]))
    result[lang[xx[0]]][job[xx[1]]][stage[xx[2]]][soul['-']].append(int(xx[4]))
    result[lang[xx[0]]][job[xx[1]]][stage['-']][soul[xx[3]]].append(int(xx[4]))

for a in range(4):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                result[a][b][c][d].sort()

for i,y in enumerate(query):
    val = y.replace('and',' ')
    yy=val.split()
    
    vs[i]=(len(result[lang[yy[0]]][job[yy[1]]][stage[yy[2]]][soul[yy[3]]])-bisect.bisect_left(result[lang[yy[0]]][job[yy[1]]][stage[yy[2]]][soul[yy[3]]],int(yy[4])))
print(vs)

##############################################################################################################################################################


import bisect
import collections


def solution(info, query):
    scores_by_type = collections.defaultdict(list)
    for resume in info:
        *types, score = resume.split()
        scores_by_type[tuple(types)].append(int(score))
    for scores in scores_by_type.values():
        scores.sort()

    answer = []
    for q in query:
        q_list = q.split()
        type_filter = q_list[::2]
        score_filter = int(q_list[-1])
        count = sum(
            len(scores) - bisect.bisect_left(scores, score_filter)
            for types, scores in scores_by_type.items()
            if all(f in ['-', t] for f, t in zip(type_filter, types)))
        answer.append(count)

    return answer

### 이것과 별개로 itertools 공부좀 빡세게 해야겠다.