class Solution:
    # solution 2: lenth-prefixing

    def encode(self, strs: List[str]) -> str:
        encode = "".join(f"{len(s)}_{s}" for s in strs) 
        print(f"encode:{encode}")
        return encode

    def decode(self, s: str) -> List[str]:
        print(f"decode, input:{s}")
        res, num = [], []
        n = len(s)
        i = 0
        while i < n:
            length = 0
            if s[i] == '_':
                print(num)
                length = int("".join(num))
                res.append(s[i+1:i+1+length])
                i = i + length + 1
                num = []
                continue
                
            num.append(s[i])
            i += 1

        return res