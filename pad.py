def solution(m, musicinfos):
    answer = '(None)'
    ltn=[]
    idx=0
    length=0
    while idx<len(m):
        if idx+1<len(m) and m[idx+1]=='#':
            ltn.append(m[idx:idx+2])
            idx+=2
        else:
            ltn.append(m[idx:idx+1])
            idx+=1
    for msi in musicinfos:
        msi=msi.split(',')
        st,et,song,melody=msi[0],msi[1],msi[2],msi[3]
        st=st.split(':')
        et=et.split(':')
        stotal=int(st[0])*60+int(st[1])
        etotal=int(et[0])*60+int(et[1])
        ttotal=etotal-stotal
        idx=0
        mel=[]
        while idx<len(melody):
            if idx+1<len(melody) and melody[idx+1]=='#':
                mel.append(melody[idx:idx+2])
                idx+=2
            else:
                mel.append(melody[idx:idx+1])
                idx+=1
        mtotal=[]
        if len(mel)>ttotal:
            mtotal=mel[:ttotal]
        else:
            mtotal+=mel[:]
            ttotal-=len(mel)
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
                    length=mtotal
                    answer=song
                    break


    return answer

print(solution('ABC',['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))