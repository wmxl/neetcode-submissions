class Solution:
    def characterReplacement(self, a: str, k: int) -> int:
        n = len(a)
        if k >= n - 1 or n <= 1:
            return n
        d = {}
        for c in a:
            d[c] = 0

        i = j = 0
        maxd = 0
        while j < k + maxd and j < n:
            # print('loop1')
            c = a[j]
            d[c] += 1
            if d[c] > maxd:
                maxd = d[c]
            j += 1

        while i < n and j < n:
            # print('loop3')
            c = a[j]
            d[c] += 1
            if d[c] > maxd:
                maxd = d[c]
            else:                
                d[a[i]] -= 1
                i += 1             
            j += 1

        return j - i 
        