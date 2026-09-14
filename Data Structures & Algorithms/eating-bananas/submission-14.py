class Solution:
    def minEatingSpeed(self, p: List[int], h: int) -> int:
        def cal(k):
            t = 0
            for i in p:
                t += (i - 1) // k + 1
            print(f"k:{k} {t}")
            return t

        ma = p[0]
        tol = 0
        for i in p:
            tol += i
            ma = max(ma, i)
        mi = max(1,tol // h)
        print(mi, ma)

        l,r = mi,ma
        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if h < cal(m):
                l = m + 1
                if cal(m + 1) <= h:
                    return m + 1
            elif cal(m) <= h:
                r = m - 1
                if m - 1 > 0 and cal(m - 1) > h or m - 1 == 0:
                    return m
                
        return ma

