class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        def c2n(c):
            return ord(c) - ord('a')

        d = [0] * 26
        d2 = [0] * 26

        matched = 26

        for c in s1:
            d[c2n(c)] += 1
            if d[c2n(c)] == 1:
                matched -= 1

        i = j = 0
        # print(f'd:{d}')
        while j < n2:
            c = s2[j]
            c2 = s2[i]
            d2[c2n(c)] += 1 
            if d2[c2n(c)] == d[c2n(c)]:
                    matched += 1
            if d2[c2n(c)] - 1 == d[c2n(c)]:
                matched -= 1
            # print(f'c:{c} mached:{matched} d2:{d2}')
            if matched == 26:
                return True

            if j - i + 1 == n1:
                i += 1
                d2[c2n(c2)] -= 1
                if d2[c2n(c2)] == d[c2n(c2)]:
                    matched += 1
                if d2[c2n(c2)] + 1 == d[c2n(c2)]:
                    matched -= 1

            j += 1     
        return False
             