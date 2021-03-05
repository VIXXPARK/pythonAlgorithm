def solution(skill, skill_trees):
    answer = 0
    skill=list(skill)
    for combo in skill_trees:
        cur=0
        for sk in combo:
            if sk in skill[cur:]:
                if skill[cur]==sk:
                    cur+=1
                else:               # for - else 문은 for 문이 break 등으로 끊기지 않고 끝까지 수행되면
                    break           # else문으로 실행되는 문
        else:
            answer+=1
    return answer