class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        if n <= 1:
            return 0

        def area(i, j):
            return min(h[i],h[j]) * (j - i)

        i = 0
        j = n - 1
        best = area(i, j)
        while i < j:
            best = max(best, area(i, j))
            if h[i] <= h[j]:
                i += 1
            else:
                j -= 1
        return best
    