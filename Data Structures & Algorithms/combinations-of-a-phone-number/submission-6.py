class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        d = defaultdict(list)
        a = 'a'
        for i in range(2, 10):
            d[i].append(a)
            a = chr(ord(a) + 1)
            d[i].append(a)
            a = chr(ord(a) + 1)
            d[i].append(a)
            a = chr(ord(a) + 1)
            if i == 7:
                d[i].append(a)
                a = chr(ord(a) + 1)
        d[9].append('z')

        def dfs(s, i, path):
            if i == len(s):
                if len(s) > 0:
                    ans.append("".join(path))
                return 
            num = int(s[i])
            for c in d[num]:
                path.append(c)
                dfs(s, i+1, path)
                path.pop()

        dfs(digits, 0, [])
    
        return ans

        

        