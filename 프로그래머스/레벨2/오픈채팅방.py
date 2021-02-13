def solution(records):
    answer = []
    infos=[]
    dic={}
    for record in records:
        record=record.split()
        if record[0]=='Enter':
            infos.append([record[0],record[1]])
            dic[record[1]]=record[2]
        elif record[0]=='Leave':
            infos.append([record[0],record[1]])
        else:
            dic[record[1]]=record[2]
    for info in infos:
        if info[0]=='Enter':
            ans=dic[info[1]]+"님이 들어왔습니다."
            answer.append(ans)
        else:
            ans=dic[info[1]]+"님이 나갔습니다."
            answer.append(ans)
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	))