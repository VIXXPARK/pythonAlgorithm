class Solution:
    def trap(self, height) -> int:
        dic = {}
        num = set()
        visited = [False]*(len(height))
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
            for idx in range(len(dic[h])-1):
                wall = height[dic[h][idx]]
                for domain in range(dic[h][idx]+1, dic[h][idx+1]):
                    if not visited[domain]:
                        visited[domain] = True
                        ans += wall-height[domain]
            value = num[-1] if num else 0
            for idx in dic[h]:
                height[idx] = value
            if dic.get(value, 0):
                dic[value] += dic[h][:]
        return ans


s = Solution()

print(s.trap([4, 2, 3]))
