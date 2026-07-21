class Solution:
    sep = '\x1c'
    def encode(self, strs: List[str]) -> str:
        
        parts = []
        for s in strs:
            parts.append(s)
            parts.append(self.sep)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        
        res = []
        word = ""
        for c in s:
            if c == self.sep:
                res.append(word)
                word = ""
                continue
            word += c
        return res



