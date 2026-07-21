class Solution:
    sep = '_'

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            new_s = s.replace('/', '//')
            new_s1 = new_s.replace(self.sep, '/' + self.sep)
            parts.append(new_s1)
            parts.append(self.sep)
        st = "".join(parts)
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '/':
                word += s[i+1]
                i += 2
                continue

            elif s[i] == self.sep:
                res.append(word)
                word = ""
                i += 1
                continue

            word += s[i]
            i += 1

        return res