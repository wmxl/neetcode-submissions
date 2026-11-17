class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        a = []
        v = [False] * l

        d = defaultdict(int)
        uniques = []
        for n in nums:
            d[n] += 1
            if d[n] == 1:
                uniques.append(n)
        # print(d)
        # print(uniques)

        l = len(d)

        def dfs(i):
            if i == l:
                print(a)
                ans.append(a[:])
                return 
        
            for j in range(d[uniques[i]] + 1):
                for k in range(j):
                    a.append(uniques[i])
                dfs(i+1)
                for k in range(j):
                    a.pop()
                
                
        dfs(0)

        return ans
