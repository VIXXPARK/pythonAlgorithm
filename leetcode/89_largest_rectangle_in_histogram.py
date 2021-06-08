class Solution:
    def largestRectangleArea(self, heights) -> int:
        stack = [-1]
        heights.append(0)
        lst=[]
        lst.append(heights[0])
        for idx in range(len(heights)):
            while stack and heights[idx] <= heights[stack[-1]]:
                loc = stack.pop()
                if stack:
                    lst.append((idx-1-stack[-1])*heights[loc])
            stack.append(idx)
        return max(lst)