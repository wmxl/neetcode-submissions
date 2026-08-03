class Solution:
    def characterReplacement(self, a: str, kk: int) -> int:
        n = len(a)
        exist = set()
        d = {}
        if kk >= n - 1 or n <= 1:
            return n
        
        for c in a:
            d[c] = 0
            exist.add(c)

        ma = 0
        for c in exist:
            k = kk
            j = i = 0
            while i < n and j < n:
                while j < n and (k > 0 or a[j] == c):
                    d[c] = d[c] + 1
                    if a[j] != c:
                        k -= 1
                    j += 1
                ma = max(ma, d[c])
                
                rep = 0 
                while i < n and a[i] == c:
                    rep += 1
                    i += 1
                
                i += 1
                k += 1
                d[c] -= (1 + rep)
                
        return ma
        