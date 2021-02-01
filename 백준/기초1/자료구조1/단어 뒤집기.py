import sys
for _ in range(int(sys.stdin.readline())):
    line = sys.stdin.readline().split()
    ans=''
    for x in (line):
        ans+=x[::-1]+ " " ## 역순으로 저장하는 법은 [::-1]
    print(ans.strip())