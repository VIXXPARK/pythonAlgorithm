def solution(lines):
    answer = 0
    segment=[]
    for line in lines:
        ymd,hms,ss=line.split()
        h,m,s=hms.split(':')
        h,m,s=int(h),int(m),float(s)
        ss=float(ss[:-1])
        beforeTime=h*60*60+m*60+s
        afterTime=round(beforeTime-ss+0.001,3)
        segment.append([afterTime,beforeTime])
    for seg in segment:
        left=[seg[0],round(seg[0]+1-0.001,3)]
        right=[seg[1],round(seg[1]+1-0.001,3)]
        val=0
        for x in segment:
            if x[0]<=left[0]<=x[1] or left[0]<=x[0]<=left[1] or x[0]<=left[1]<=x[1] or (x[0]<=left[0] and left[1]<=x[1]):
                val+=1
        answer=max(answer,val)
        val=0
        for x in segment:
            if x[0]<=right[0]<=x[1] or right[0]<=x[0]<=right[1] or x[0]<=right[1]<=x[1] or (x[0]<=right[0] and right[1]<=x[1]):
                val+=1
        answer=max(answer,val)
    return answer