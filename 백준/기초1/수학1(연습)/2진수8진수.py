# num = input()
# li=[]
# ans=[]
# for i in num:
#     li.append(int(i))
# li.reverse()
# for x in range(0,len(li),3):
#     val=0
#     if x+3<=len(li):
#         for i in range(x,x+3):
#             if li[i]:
#                 val+=2**(i-x)
#     else:
#         for i in range(x,len(li)):
#             if li[i]:
#                 val+=2**(i-x)
#     ans.append(str(val))
# print(''.join(ans[::-1]))
#내가 푼 방법

print(oct(int(input(), 2))[2:])
# 모범 답안

