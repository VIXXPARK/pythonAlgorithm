# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
T=int(input())
ans=[]
for _ in range(T):
	N,M=map(int,input().split())
	count=0
	vN=N//5;vM=M//7
	if vN==0:
		ans.append(0)
		
	elif vN<=vM:
		N-=vN*5;M-=vN*7
		count+=vN
		ans.append(count)
		
	elif vN>vM:
		N-=vM*5;M-=vM*7
		count+=vM
		if M!=0 and N>=12-M:
			N-=12-M
			count+=1
		cN=N//12
		ans.append(count+cN)
			
for v in ans:
	print(v)
			