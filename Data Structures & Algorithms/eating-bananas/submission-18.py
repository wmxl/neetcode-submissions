class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        def cal(k):
            t = 0
            for i in p:
                t += (i - 1) // k + 1
            return t

        ma = p[0]
        tol = 0
        for i in p:
            tol += i
            ma = max(ma, i)
        mi = max(1, tol // h)

        if cal(1) <= h:
            return 1

        l,r = mi,ma
        while l <= r:
            m = (l + r) // 2
            # print(l, r, m)
            if h < cal(m):
                l = m + 1
                if cal(m + 1) <= h:
                    return m + 1
            else:
                r = m - 1
                if m - 1 > 0 and cal(m - 1) > h:
                    return m
                
        return ma
