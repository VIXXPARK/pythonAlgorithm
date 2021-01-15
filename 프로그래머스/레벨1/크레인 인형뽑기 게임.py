def solution(board, moves):
    answer=0
    board = list(map(list,zip(*board)))
    lst=[]
    for ord in moves:
        ord-=1
        for num in range(len(board[ord])):
            if board[ord][num]!=0:
                lst.append(board[ord][num])
                board[ord][num]=0
                if len(lst)>=2 and lst[-1]==lst[-2]:
                    answer+=2
                    lst.pop()
                    lst.pop()
                break
    return answer


##clean code ###
def solution2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
