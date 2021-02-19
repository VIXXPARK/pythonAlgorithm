def zari(val,n):
    if val==0: return '0'
    ans=''
    dic={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while val:
        ans+=dic[val%n]
        val//=n
    return ans[::-1]

def solution(n, t, m, p):
    answer = ''
    ans=''
    val=0
    cnt=0
    while len(answer)<m*t:
        answer+=zari(val,n)
        val+=1
    for i in range(p-1,len(answer),m):
        if cnt<t:
            ans+=answer[i]
        else:
            break
        cnt+=1
    return ans

print(solution(2,4,2,1))