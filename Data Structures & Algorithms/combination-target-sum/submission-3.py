class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        def dfs(start, total):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return 

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, total + nums[i])
                path.pop()
                
        dfs(0, 0)
        return ans