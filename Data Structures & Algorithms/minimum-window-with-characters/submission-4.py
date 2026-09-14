class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def judge(dt, ds):
            for k in dt:
                if ds[k] < dt[k]:
                    return False
            return True
        ns,nt = len(s),len(t)
        if ns < nt:
            return ""
        dt = defaultdict(int)
        ds = defaultdict(int)
        for c in t:
            dt[c] += 1
        for c in s:
            ds[c] += 1
        if not judge(dt, ds):
            return ""

        i, j = 0, ns - 1
        while ds[s[j]] - 1 >= dt[s[j]]:
            ds[s[j]] -= 1
            j -= 1
            
        while ds[s[i]] - 1 >= dt[s[i]]:
            ds[s[i]] -= 1
            i += 1
            
        fi, fj = i, j
        # print(f'init i:{i} j:{j}')

        while j < ns:
            ds[s[i]] -= 1
            while judge(dt, ds):
                i += 1
                fi, fj = i, j
                ds[s[i]] -= 1
                # print({k: v for k, v in ds.items() if v > 0})
                # print(f'fi:{i} fj:{j}')
            i += 1
            j += 1
            if j < ns:
                ds[s[j]] += 1
            # print({k: v for k, v in ds.items() if v > 0})

        output = s[fi:fj+1]
        return output