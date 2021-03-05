# n: 전체 원소의 개수
# picked: 지금까지 고른 원소들의 번호
# toPick: 더 고를 원소의 개수 
# 일 때, 앞으로 toPick개의 원소를 고르는 모든 방법을 출력한다.

def pick(n:int,picked:list,toPick:int):
    if not toPick:
        print(picked)
        return
    back = 0 if not picked else picked[-1]+1
    for i in range(back,n):
        picked.append(i)
        pick(n,picked,toPick-1)
        picked.pop()

pick(5,[],4)