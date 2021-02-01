# import sys
# input=sys.stdin.readline
# N,K=map(int,input().split())
# alpha=[False]*26
# alpha[0],alpha[2],alpha[13],alpha[19],alpha[8]=True,True,True,True,True
# words=[]
# for _ in range(N):
#     val=input().strip()
#     words.append(val[4:len(val)-4])

# def func(alphaBet,count):
#     global ans
#     if count==K:
        
#         ret=0
#         for word in words:
#             flag=True
#             for i in word:
#                 if not alpha[ord(i)-ord('a')]:
#                     flag=False
#             if flag:
#                 ret+=1
#         ans=max(ans,ret)
#         return
        
#     for i in range(alphaBet,26):
#         if not alpha[i]:
#             alpha[i]=True
#             func(i,count+1)
#             alpha[i]=False
# if K<5:
#     print(0)
# elif K==26:
#     print(N)
# else:
#     K-=5
#     ans=0
#     func(0,0)
#     print(ans)

##### Quick Version #####
num_of_words, num_of_teaching = map(int, input().split())
num_of_teaching -= 5

bit = {}
for i in range(26):
	bit[chr(ord('a') + i)] = 1 << i

def word_to_bit(word):
	result = 0
	for char in word:
		result |= bit[char]
	return result
	
words, remain = [], set()
poss, imposs = 0, 0

for _ in range(num_of_words):
	word = set(input()[4:-4]) - set(['a', 'n', 't', 'i', 'c'])
	if len(word) == 0:
		poss += 1
	elif len(word) > num_of_teaching:
		imposs += 1
	else:
		remain |= word # or 연산후 할당 
		words.append(word_to_bit(word))
remain = list(remain)

def teach(lst, mask, k):
	if k < 0: ## 단어 수가 5보다 부족할 때
		return 0
	elif k == 0:
		result = poss
		for word in words:
			if word & mask == 0:
				result += 1
		return result
	else:
		result = 0
		for i in range(len(lst) - k + 1):
			result = max(result, teach(lst[i+1:], mask ^ bit[lst[i]], k - 1))
		return result

if num_of_teaching < len(remain):
	print(teach(remain, ((1 << 26) - 1), num_of_teaching))
else:
	print(num_of_words - imposs)