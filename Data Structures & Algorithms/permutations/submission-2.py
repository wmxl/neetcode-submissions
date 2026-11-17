class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        ans = []
        a = [0] * l
        v = [False] * l

        def dfs(i):
            if i == l:
                ans.append(a[:])
                return 
            
            for j in range(l):
                if v[j]: continue

                a[i] = nums[j]
                v[j] = True
                dfs(i+1)
                v[j] = False

        dfs(0)

        return ans

        