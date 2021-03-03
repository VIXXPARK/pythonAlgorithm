# def solution(prices):
#     answer = []
#     prices=prices[::-1]
#     val=[-1 for _ in range(max(prices)+1)]
#     for idx,x in enumerate(prices):
#         flag=True
#         minval=0
#         for i in range(x-1,-1,-1):
#             if val[i]!=-1:
#                 flag=False
#                 minval=max(minval,val[i])
#         if flag:
#             answer.insert(0,idx)
#         else:
#             answer.insert(0,idx-minval)
#         val[x]=idx
#     return answer



def solution(prices):
    answer = []
    count=0
    val=100000
    for i in range(len(prices)-1,-1,-1):
        if count==0:
            answer.insert(0,0)
            val=prices[i]
            count+=1
        else:
            if val<prices[i]:
                x=-1
                for idx in range(1,count+1):
                    if prices[i]>prices[i+idx]:
                        x=idx
                        break
                count+=1
                if x==-1:
                    answer.insert(0,count-1)
                else:
                    answer.insert(0,x)
            else:
                count+=1
                answer.insert(0,count-1)
                val=prices[i]

    return answer

print(solution([1, 2, 3, 2, 3]))