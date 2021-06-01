class Solution:
    def trap(self, height) -> int:
        dic = {}  # 각 높이의 값을 가진 위치 저장
        num = set()  # 높이 값 저장
        visited = [False]*(len(height))  # 계산 유무 판단
        ans = 0
        for idx, val in enumerate(height):
            if dic.get(val, 0) == 0:
                dic[val] = [idx]
            else:
                dic[val].append(idx)
            num.add(val)
        num = list(num)
        num.sort()
        while num:
            h = num.pop()
            if h == 0:
                break
            dic[h].sort()
            for idx in range(len(dic[h])-1):  # 웅덩이 계산
                wall = height[dic[h][idx]]
                for domain in range(dic[h][idx]+1, dic[h][idx+1]):
                    if not visited[domain]:
                        visited[domain] = True
                        ans += wall-height[domain]
            value = num[-1] if num else 0  # num이 없을 때를 고려
            for idx in dic[h]:  # 높이 하향
                height[idx] = value
            if dic.get(value, 0):
                dic[value] += dic[h][:]
                tmp = []
                for val in dic[value]:  # 이미 방문한 높이는 제외
                    if not visited[val]:
                        tmp.append(val)
                dic[value] = tmp[:]
        return ans

######################################################################


def trap(self, bars):
    if not bars or len(bars) < 3:
        return 0
    volume = 0
    left, right = 0, len(bars) - 1
    l_max, r_max = bars[left], bars[right]
    while left < right:
        l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
        if l_max <= r_max:
            volume += l_max - bars[left]
            left += 1
        else:
            volume += r_max - bars[right]
            right -= 1
    return volume

##################################################################


def trap(height):
    waterLevel = []
    left = 0
    for h in height:
        left = max(left, h)
        waterLevel += [left]  # over-fill it to left max height
    right = 0
    for i, h in reversed(list(enumerate(height))):
        right = max(right, h)
        waterLevel[i] = min(waterLevel[i], right) - \
            h  # drain to the right height
    return sum(waterLevel)
