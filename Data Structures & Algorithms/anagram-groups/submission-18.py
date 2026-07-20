import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getKey(d: dict) -> str:

            parts = []
            for c in string.ascii_lowercase:
                if c in d:
                    parts.append(c + str(d[c]))
            return "".join(parts)

        big_d = {}

        for _, s in enumerate(strs):
            d = {}
            for c in s:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
        
            key = getKey(d)

            if key in big_d:
                big_d[key].append(s)
            else:
                big_d[key] = [s]

        values = list(big_d.values())
        return values

            
