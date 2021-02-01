import sys
pri = [True]*1000001
pri[0]=False
pri[1]=False
for i in range(2,int((1000001)**0.5)):
    if pri[i]==True:
        for j in range(i*i,1000001,i):
            pri[j]=False
for _ in range(int(sys.stdin.readline().rstrip())):
    val=int(sys.stdin.readline().rstrip())
    ans=0
    for x in range(2,int((val+1)//2)+1):
        if pri[x]==True and pri[val-x]==True:
            ans+=1
    print(ans)

# import sys


# def makePrimeList(is_prime):
#     primes = []
#     for i in range(2, 1000001):
#         if is_prime[i]:
#             primes.append(i)
#             for j in range(i * 2, 1000001, i):
#                 is_prime[j] = False
#     return primes

# def getPartition(number, primes, is_prime):
#     count = 0
#     for a in primes:
#         b = number - a
#         if a > b:
#             break
#         else:
#             if is_prime[b]:
#                 count += 1
#     return count


# def main():
#     is_prime = [True for _ in range(1000001)]
#     is_prime[0] = False
#     is_prime[1] = False

#     T = int(sys.stdin.readline().rstrip())
#     primes = makePrimeList(is_prime)
#     for _ in range(T):
#         num = int(sys.stdin.readline().rstrip())
#         answer = getPartition(num, primes, is_prime)
#         print(answer)


# if __name__ == "__main__":
#     main()
