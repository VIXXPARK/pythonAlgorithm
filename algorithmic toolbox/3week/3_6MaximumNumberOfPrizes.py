n=int(input())
def increSum(n):
    return (n*(n+1))//2
x=int(n**0.5) # 루트
while True:
    N=increSum(x) # 1-x 까지의 합
    if x<n-N: # Input 값에서 N 뺀 값이 x값보다 크면 1증가
        x+=1
    else:
        lst=[i for i in range(1,x)]+[n-increSum(x-1)] # 1 부터 x-1 까지 + [n-(1~x-1)] 로 리스트를 만든다.
        print(len(lst))
        print(' '.join(map(str,lst)))    
        quit()


