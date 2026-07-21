class Solution:

    def encode(self, strs: List[str]) -> str:
        sep = chr(1) 
        parts = []
        for s in strs:
            parts.append(s)
            parts.append(sep)
        return "".join(parts)


    def decode(self, s: str) -> List[str]:
        sep = chr(1) 
        res = []
        word = ""
        for c in s:
            if c == sep:
                res.append(word)
                word = ""
                continue
            word += c
        return res



