def partition(m,ltn):
    idx=0
    while idx<len(m):
        if idx+1<len(m) and m[idx+1]=='#':
            ltn.append(m[idx:idx+2])
            idx+=2
        else:
            ltn.append(m[idx:idx+1])
            idx+=1

def solution(m, musicinfos):
    answer = '(None)'
    ltn=[]
    length=0 #longest melody
    partition(m,ltn) #insert ltn
    for msi in musicinfos:
        msi=msi.split(',')
        st,et,song,melody=msi[0],msi[1],msi[2],msi[3]
        st=st.split(':')
        et=et.split(':')
        stotal=int(st[0])*60+int(st[1])
        etotal=int(et[0])*60+int(et[1])
        ttotal=etotal-stotal
        mel=[]
        partition(melody,mel) #insert mel
        mtotal=[]
        if len(mel)>=ttotal:
            mtotal=mel[:ttotal]
        else:
            while ttotal:
                if ttotal>len(mel):
                    mtotal+=mel[:]
                    ttotal-=len(mel)
                else:
                    mtotal+=mel[:ttotal]
                    ttotal=0
        for i in range(0,len(mtotal)-len(ltn)+1):
            if ltn==mtotal[i:i+len(ltn)]:
                if length<len(mtotal):
                    length=len(mtotal)
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