# import sys
# def gcd(left,right):
#     if right==0:
#         return left
#     return gcd(right,left%right)


# testCase = int(input())
# for _ in range(testCase):
#     N,M,fx,fy=map(int,sys.stdin.readline().rstrip().split())
#     x,y=1,1
#     count=1
#     if M>N:
#         big=M
#         small=N
#     else:
#         big=N
#         small=M
#     total=(big*small)/gcd(big,small)
#     while True:
#         if count>total:
#             print(-1)
#             break
#         if fx==x and fy==y:
#             print(count)
#             break

#         if count==1:
#             x=fx
#             if(1+fx-x)%M!=0:
#                 y=(1+fx-1)%M  
#             else: y=M
#             count=fx
#         else:
#             if (y+N)%M!=0:
#                 y=(y+N)%M
#             else: y=M
#             count+=N

def num(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1

t = int(input())
for i in range(t):
    m, n, x, y = map(int, input().split())
    print(num(m, n, x, y))

#https://pacific-ocean.tistory.com/126