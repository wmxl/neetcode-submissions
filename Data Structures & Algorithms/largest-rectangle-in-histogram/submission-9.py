class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        h.append(0)
        n = len(h)
        stack = []
        ma = 0
        for i, e in enumerate(h):
            top = i
            while stack and h[stack[-1]] >= e:
                top = stack.pop()
                ma = max(ma, h[top] * (i - top))
            h[top] = e
            stack.append(top)

        return ma