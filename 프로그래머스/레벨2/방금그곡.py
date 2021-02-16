def solution(m, musicinfos):
    answer = []
    store=[]
    k=0
    maxPlaying=0
    while k<len(m):
        if k+1<len(m) and m[k+1]=='#':
            store.append(m[k:k+2])
            k+=2
        else:
            store.append(m[k:k+1])
            k+=1
    for musicinfo in musicinfos:
        startTime,endTime,song,melody=musicinfo.split(',')
        startHour,startMin=map(int,startTime.split(':'))
        endHour,endMin=map(int,endTime.split(':'))
        
        tempo=[]
        playing=[]
        i=0
        while i<len(melody):
            if i+1<len(melody) and melody[i+1]=='#':
                tempo.append(melody[i:i+2])
                i+=2
            else:
                tempo.append(melody[i:i+1])
                i+=1
                
        totalLength=(endHour-startHour)*60+(endMin-startMin)
        playTime=totalLength
        
        if totalLength>len(tempo):
            playing=tempo[:]
            totalLength-=len(tempo)
            while  totalLength>0:
                if totalLength-len(tempo)>=0:
                    playing+=tempo[:]
                    totalLength-=len(tempo)
                elif totalLength>0:
                    playing+=tempo[:totalLength]
                    totalLength=0
        else:
            playing=tempo[:totalLength]
            
        
        for x in range(0,len(playing)-len(store)+1):
            if store==playing[x:x+len(store)]:
                answer.append([playTime,song])
                maxPlaying=max(playTime,maxPlaying)
                break
        
    if len(answer)==0:
        return "(None)"
    else:
        xx=[]
        for ans in answer:
            if ans[0]==maxPlaying:
                xx.append(ans[1])
        return xx[0]

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