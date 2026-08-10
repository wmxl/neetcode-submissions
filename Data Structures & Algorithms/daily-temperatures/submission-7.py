class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        stack, output = [], [0] * n
        for i, cur in enumerate(t):
            while stack and t[stack[-1]] < cur:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output
        