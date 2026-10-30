class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(start):
            s = 0
            for p in path:
                s += p
            if s == target:
                ans.append(path[:])
                return
            if s > target:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i)
                path.pop()
        dfs(0)
        return ans