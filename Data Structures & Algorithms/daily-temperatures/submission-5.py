class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        i = n - 1
        stack, output = [], []
        while i >= 0:
            while stack and t[stack[-1]] <= t[i]:
                stack.pop()
            if not stack:
                output.append(0)
            else:
                output.append(stack[-1] - i)
            stack.append(i)
            i -= 1
        output.reverse()
        return output