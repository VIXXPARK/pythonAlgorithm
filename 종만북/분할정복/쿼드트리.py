#quadtree
def quad(loctree, ind):
    let = loctree[ind]  # 인덱스 번째의 글자
    if let == 'w' or let == 'b':  # 상하 바꿔도 변함이 없음
        return let
    # let이 w나 b가 아닌 경우=let이 x일때
    ind += 1  # x가 나온 위치로부터 1칸 뒤
    a=quad(tree,ind)
    ind += len(a)  # 왼쪽 위가 차지하는 칸수 만큼 뒤
    b=quad(tree,ind)
    ind += len(b)  # 오른 위가 차지하는 칸수 만큼 뒤
    c=quad(tree,ind)
    ind += len(c)  # 왼쪽 아래가 차지하는 칸수 만큼 뒤
    d=quad(tree,ind)
    return 'x'+c+d+a+b
 
 
case = int(input())
for i in range(case):
    tree = input()
    print(quad(tree, 0))  # 인덱스=0
