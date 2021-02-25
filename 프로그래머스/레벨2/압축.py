def solution(msg):
	answer = []
	dicNum=1
	dic={}
	for i in range(26):
		dic[chr(65+i)]=dicNum
		dicNum+=1
	start,i=0,0
	while i<len(msg):
		while i<len(msg) and dic.get(msg[start:i+1],0):
			i+=1
		answer.append(dic[msg[start:i]])
		dic[msg[start:i+1]]=dicNum
		dicNum+=1
		start=i       
	return answer

print(solution('KAKAO'))