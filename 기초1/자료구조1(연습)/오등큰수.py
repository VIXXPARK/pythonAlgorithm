import sys

num = int(input())
a = list(map(int, input().split(" ")))
result = ["-1" for _ in range(num)]
stack = [0]
count = dict()
for i in a:
    try:
        count[i] += 1
    except:
        count[i] = 1

for i in range(num):
    while stack and count[a[stack[-1]]] < count[a[i]]:
        result[stack[-1]] = str(a[i])
        stack.pop()
    stack.append(i)
    i+=1

print(" ".join(result))