class Solution:
    def characterReplacement(self, a: str, k: int) -> int:
        n = len(a)
        d = {}
        for c in a:
            d[c] = 0

        i = j = 0
        maxd = 0
        while j < n:
            c = a[j]
            d[c] += 1
            if d[c] > maxd:
                maxd = d[c]
            if j - i + 1 - maxd > k: # 'windows len - maxd = k' is legal
                d[a[i]] -= 1
                i += 1
            j += 1

        return n - i 
        