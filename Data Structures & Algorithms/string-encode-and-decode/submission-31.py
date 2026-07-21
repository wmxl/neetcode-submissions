class Solution:
    sep = '_'

    def encode(self, strs: List[str]) -> str:
        return "".join(s.replace('/', '//').replace(self.sep, '/' + self.sep) + self.sep for s in strs)

    def decode(self, s: str) -> List[str]:
        res, word = [], []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '/':
                word.append(s[i+1])
                i += 2
                continue

            elif s[i] == self.sep:
                res.append("".join(word))
                word = []
                i += 1
                continue

            word.append(s[i])
            i += 1

        return res