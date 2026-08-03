class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        d = {}
        for c in s1:
            d[c] = 0
        for c in s1:
            d[c] += 1
        d2 = {}
        i = j = 0
        while j < n2:
            c = s2[j]
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1

            if j - i + 1 == n1:
                if d == d2:
                    return True
                print(f'i:{i} j:{j} d2:{d2}')
                d2[s2[i]] -= 1
                if d2[s2[i]] == 0:
                    del d2[s2[i]]
                i += 1
            j += 1

        return False
             