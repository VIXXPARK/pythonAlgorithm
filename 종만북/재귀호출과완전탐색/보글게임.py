word="pretty"
dic={}
for w in word:
    dic[w]=dic.get(w,0)+1
length=5
board=[['u','r','l','p','m'],['x','p','r','e','t'],['g','i','a','e','t'],['x','t','n','z','y'],['x','o','q','r','s']]
def boggle(y,x,dic,step,n):
    if step==n:
        return True
    dy=[-1,-1,-1,0,1,1,1,0]
    dx=[-1,0,1,1,1,0,-1,-1]
    for i in range(8):
        fy=y+dy[i]
        fx=x+dx[i]
        if 0<=fx<length and 0<=fy<length:
            if  dic.get(board[fy][fx],0):
                dic[board[fy][fx]]-=1
                if boggle(fy,fx,dic,step+1,n):
                    return True
                dic[board[fy][fx]]+=1
    
    
def solution():
    flag=True
    for i in range(5):
        for j in range(5):
            if dic.get(board[i][j],0):
                dic[board[i][j]]-=1
                if boggle(i,j,dic,1,6):
                    flag=False
                    break
                dic[board[i][j]]+=1
        if not flag:
            return True
    return False
    

print(solution())

                

            


