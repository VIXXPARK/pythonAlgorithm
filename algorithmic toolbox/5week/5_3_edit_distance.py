lst=list(input())
lst2=list(input())
n=len(lst)
m=len(lst2)
dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
for i in range(m+1):
    dp[0][i]=i
for i in range(n+1):
    dp[i][0]=i

def lcs(a,b):
    for i in range(1,n+1):
        for j in range(1,m+1):
            if lst[i-1]==lst2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n][m]
print(lcs(0,0))
for i in range(n+1):
    print(dp[i])



########################################
def edit_distance(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l2 > l1:
        return edit_distance(s2, s1)
    if l2 is 0:
        return l1
    prev_row = list(range(l2 + 1))
    current_row = [0] * (l2 + 1)
    for i, c1 in enumerate(s1):
        current_row[0] = i + 1
        for j, c2 in enumerate(s2):
            d_ins = current_row[j] + 1
            d_del = prev_row[j + 1] + 1
            d_sub = prev_row[j] + (1 if c1 != c2 else 0)
            current_row[j + 1] = min(d_ins, d_del, d_sub)
        prev_row[:] = current_row[:]
    return prev_row[-1]
s1="short"
s2="ports"
print(edit_distance(s1,s2))
