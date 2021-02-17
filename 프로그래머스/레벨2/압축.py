def alphaDic(dic,dicNum):
    for i in range(1,27):
        dic[chr(ord('A')+i-1)]=i
        dicNum+=1
    return dic,dicNum

def solution(msg):
    answer = []
    dic={}
    dicNum=0
    dic,dicNum=alphaDic(dic,dicNum)
    i=0
    start=0
    while i<len(msg):
        while i<len(msg) and dic.get(msg[start:i+1],0):
            i+=1
        if start==len(msg)-1:
            answer.append(dic[msg[start]])
            break
        if len(msg[start:i])==1:
            answer.append(dic[msg[start]])
            dic[msg[start:i+1]]=dicNum+1
            dicNum+=1
            start+=1
        else:
            answer.append(dic[msg[start:i]])
            dic[msg[start:i+1]]=dicNum+1
            dicNum+=1
            start=i
            
    return answer