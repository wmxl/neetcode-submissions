class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        order = sorted(range(n), key = lambda i : p[i])
        p = [p[i] for i in order]
        s = [s[i] for i in order]
        i = 0
        cnt = 0
        while i < n:
            time = (t - p[i])/s[i]
            j = i + 1
            while j < n and p[j] + time * s[j] > t:
                j += 1
            else:
                if j == n:
                    i += 1
                else:
                    cnt += (j - i)
                    i = j
        return n - cnt