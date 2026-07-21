class Solution:
    sep = '_'
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            new_s = s.replace(self.sep, '/' + self.sep)
            parts.append(new_s)
            parts.append(self.sep)
        st = "".join(parts)
        print(st)
        return st

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '/' and i + 1 < n and s[i+1] == self.sep:
                if i + 1 == n - 1:
                    word += s[i]
                    i += 1
                    continue

                word += self.sep
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