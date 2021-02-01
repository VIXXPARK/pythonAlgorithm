import sys
n = int(sys.stdin.readline())
seq = sys.stdin.readline().rstrip().split(' ')
seq = [int(x) for x in seq]
end = 0
findPoint = False
for i in range(len(seq)-1, 0, -1):
    if seq[i-1] < seq[i]:
        end = i-1
        findPoint = True
        break
if findPoint == True:
    for j in range(len(seq)-1, end, -1):
        if seq[end] < seq[j]:
            seq[j], seq[end] = seq[end], seq[j]
            break
    seq = seq[:end+1] + seq[len(seq)+1:end:-1]
    sys.stdout.write(' '.join(map(str,seq))+'\n')
else:
    print(-1)