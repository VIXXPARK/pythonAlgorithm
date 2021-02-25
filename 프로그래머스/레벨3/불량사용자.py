import re,collections
count=0
world={}
def find(bancnt,depth,ans):
    global world
    if depth==len(bancnt):
        tmp=[]
        for k,v in ans.items():
            if v>=2:
                return
            if v!=0:
                tmp.append(k)
        tmp.sort()
        world[''.join(tmp)]=1
    else:
        for val in bancnt[depth]:
            if ans.get(val,0)==0:
                ans[val]=ans.get(val,0)+1
                find(bancnt,depth+1,ans)
                ans[val]-=1
                
def solution(user_id, banned_id):
    global world,count
    answer = 1
    banned=[]
    bancnt=[]
    for ban in banned_id:
        tmp=''
        for b in ban:
            if b!='*':
                tmp+=b
            else:
                tmp+='[\w]{1}'
        banned.append(tmp)
    for idx,ban in enumerate(banned):
        cnt=[]
        for user in user_id:
            if len(banned_id[idx])==len(user):
                x=re.match(ban,user)
                if x:
                    cnt.append(user)
        bancnt.append(cnt)

    find(bancnt,0,{})
    for k,v in world.items():
        count+=v
    return count

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
#############################################################################################################
def combi(temp, number, calculate):
    global result
    if len(temp) == len(calculate):
        temp = set(temp)
        if temp not in result:
            result.append(temp)
        return
    else:
        for j in range(len(calculate[number])):
            if calculate[number][j] not in temp:
                temp.append(calculate[number][j])
                combi(temp, number+1, calculate)
                temp.pop()
result = []
def solution2(user_id, banned_id):
    global result
    calculate = []
    for ban in banned_id:
        possible=[]
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                count = 0
                for i in range(len(ban)):
                    if user[i] == ban[i]:
                        count+=1
                if count == len(ban)-ban.count('*'):
                    possible.append(user)
        calculate.append(possible)

    combi([], 0, calculate)
    return len(result)