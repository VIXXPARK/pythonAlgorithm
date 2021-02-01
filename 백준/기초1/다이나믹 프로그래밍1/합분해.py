import sys 
N, K = map(int, sys.stdin.readline().split()) 
mod = 1000000000 
table = [1] 
table += [0] * N 
for _ in range(1, K+1): 
    for idx in range(1, N+1): 
        table[idx] = (table[idx] + table[idx-1])%mod 
sys.stdout.write(str(table[N]))

#https://suri78.tistory.com/105 참고
