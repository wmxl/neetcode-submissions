class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        n = len(p)
        order = sorted(range(n), key = lambda i : p[i], reverse = True)
        p = [p[i] for i in order]
        s = [s[i] for i in order]
        # print(p)
        # print(s)
        i = 0
        cnt = 0
        while i < n:
            # print(f"i:{i}")
            cnt += 1
            time = (t - p[i])/s[i]
            j = i + 1
            while j < n and p[j] + time * s[j] >= t:
                # print(f"j:{j}")
                j += 1
            i = j
        return cnt