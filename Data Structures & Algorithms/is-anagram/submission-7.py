class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c in d:
                d[c] -= 1
                if d[c] < 0:
                    return False
            else: 
                return False
        for c in d:
            if d[c] != 0:
                return False
        return True

