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
import bisect
def solution(info, query):
    lang={'java':0,'python':1,'cpp':2,'-':3}
    job={'backend':0,'frontend':1,'-':2}
    stage={'junior':0,'senior':1,'-':2}
    soul = {'pizza':0,'chicken':1,'-':2}
    result=[[[[ [] for soul in range(3)] for stage in range(3)]for job in range(3)]for lang in range(4)]
    vs=[0 for _ in range(len(query))]              
    for x in info:
        xx=(x.split())
        for lan in [xx[0],'-']:
            for jo in [xx[1],'-']:
                for stg in [xx[2],'-']:
                    for sul in [xx[3],'-']:
                        result[lang[lan]][job[jo]][stage[stg]][soul[sul]].append(int(xx[4]))
    for a in range(4):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    result[a][b][c][d].sort()
    for i,y in enumerate(query):
        val = y.replace('and',' ')
        yy=val.split()
        vs[i]=(len(result[lang[yy[0]]][job[yy[1]]][stage[yy[2]]][soul[yy[3]]])-bisect.bisect_left(result[lang[yy[0]]][job[yy[1]]][stage[yy[2]]][soul[yy[3]]],int(yy[4])))
    return vs
##############################################################################################################################################################


import bisect
import collections
def solution2(info, query):
    scores_by_type = collections.defaultdict(list)
    for resume in info:
        *types, score = resume.split()
        scores_by_type[tuple(types)].append(int(score))
    for scores in scores_by_type.values():
        scores.sort()

    answer = []
    for q in query:
        q_list = q.split()
        type_filter = q_list[::2] #2칸씩 뛰어넘기 
        score_filter = int(q_list[-1])
        count = sum(
            len(scores) - bisect.bisect_left(scores, score_filter)
            for types, scores in scores_by_type.items()
            if all(f in ['-', t] for f, t in zip(type_filter, types)))
        answer.append(count)

    return answer

### 이것과 별개로 itertools 공부좀 빡세게 해야겠다.

from functools import reduce
from collections import defaultdict
from bisect import insort, bisect_left

def solution3(info, query):
    table = {"c": 3, "j": 5, "p": 6, "b": 6, "f": 5, "s": 6, "-": 0}
    conv = lambda l, t: (reduce(lambda a, k: (a << 3) + t(table[k[0]]), l[:-1], 0), int(l[-1]))
    info = list(map(lambda s: conv(s.split(" "), lambda x: 7 - x), info))
    query = list(map(lambda s: conv([c for c in s.split(" ") if c != "and"], lambda x: x), query))
    d = defaultdict(list)
    for k, v in info:
        insort(d[k], v)
    return [sum([len(l) - bisect_left(l, v) for k, l in d.items() if not k & q]) for q, v in query]
