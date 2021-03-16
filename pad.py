matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix=list(map(list,zip(*matrix)))
for line in matrix:
    line.reverse()
print(matrix[:][0])