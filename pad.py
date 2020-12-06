from itertools import combinations

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
N_list = sorted(N_list) #순서대로 나오게 정렬 먼저
output = [] #중복 제거하기 위한 리스트 생성

for numbers in list(combinations(N_list, M)):
    if not output:
        output.append(numbers)
    elif numbers not in output: # 중복 제거
        output.append(numbers)
            
for numbers in output:
    for num in numbers:
        print(num, end=' ')
    print()