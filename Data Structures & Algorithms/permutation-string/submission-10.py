class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        d = collections.defaultdict(int)
        d2 = collections.defaultdict(int)

        for c in s1:
            d[c] += 1
        i = j = 0
        while j < n2:
            c = s2[j]
            d2[c] += 1
            if j - i + 1 == n1:
                if d == d2:
                    return True
                c2 = s2[i]
                d2[c2] -= 1
                if d2[c2] == 0:
                    del d2[c2]
                i += 1
            j += 1

        return False
             