import sys

strings = sys.stdin.readline().rstrip()
commands = int(sys.stdin.readline().rstrip())
left =[]
right =[]
for i in range(len(strings)):
    left.append(strings[i])

for i in range(commands):
    command = sys.stdin.readline().strip().split()
    if command[0]=='P':
        left.append(command[1])
    elif command[0]=='L':
        if len(left):
            move=left.pop()
            right.append(move)
    elif command[0]=='D':
        if len(right):
            move=right.pop()
            left.append(move)
    else:
        if len(left):
            left.pop()

print(''.join(left+right[::-1]))