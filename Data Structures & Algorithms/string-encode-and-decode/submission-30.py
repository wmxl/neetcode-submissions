class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(s.replace('/', '//') + '/;' for s in strs)

    def decode(self, s: str) -> List[str]:
        res, cur = [], []
        i, n = 0, len(s)
        while i < n:
            if s[i] == '/':
                if s[i+1] == '/':      # '//' → literal '/'
                    cur.append('/')
                else:                  # '/;' → end of a string
                    res.append("".join(cur))
                    cur = []
                i += 2
            else:
                cur.append(s[i])
                i += 1
        return res