def solution(m, musicinfos):
    answer = '(None)'
    ltn=[]
    i=0
    while i<len(m):
        if i+1<len(m) and m[i+1]=='#':
            ltn.append(m[i:i+2])
            i+=2
        else:
            ltn.append(m[i:i+1])
            i+=1
    maxLen=0
    for info in musicinfos:
        start,end,song,melody=info.split(',')
        sh,sm=map(int,start.split(':'))
        eh,em=map(int,end.split(':'))
        i=0
        tempo=[]
        music=[]
        while i<len(melody):
            if i+1<len(melody) and melody[i+1]=='#':
                tempo.append(melody[i:i+2])
                i+=2
            else:
                tempo.append(melody[i:i+1])
                i+=1
        tot=(eh-sh)*60+(em-sm)
        play=tot
        lenx=len(tempo)
        if tot>=len(tempo):
            music+=tempo
            tot-=lenx
            while tot:
                if tot-lenx>=0:
                    music+=tempo
                    tot-=lenx
                else:
                    music+=tempo[:tot]
                    tot=0
        else:
            music=tempo[:tot]
        if len(ltn)>len(music):
            continue
        else:
            for i in range(0,play-len(ltn)+1):
                if ltn==music[i:i+len(ltn)]:
                    if maxLen<play:
                        maxLen=play
                        answer=song
                        break

    return answer

############################################################################################################

def ttt(ts, te):
    tmp = (int(te.split(":")[0]) - int(ts.split(":")[0])) * 60 + int(te.split(":")[1]) - int(ts.split(":")[1])
    return tmp


def con(s):
    while s.find("#") != -1:
        a = s.find("#")
        s = s[:a - 1] + s[a - 1].lower() + s[a + 1:]
    return s


def solution2(m, musicinfos):
    m = con(m)
    ans = ''
    temp = 0
    for i in musicinfos:
        mu = i.split(',')[2]
        ss = i.split(',')[3]
        ti = ttt(i.split(',')[0], i.split(',')[1])
        ss = con(ss)
        tttt = ''
        ttmp = ti
        while ttmp > ss.__len__():
            tttt += ss
            ttmp -= ss.__len__()
        tttt += ss[:ti]
        if m in tttt and temp < ti:
            ans = mu
            temp = ti
    return ans if ans != '' else "(None)"