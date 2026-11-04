class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        ans = []
        d = {}
        nums.sort()
        def dfs(start, total):
            if total == target:
                ans.append(path[:])
                return
            if total > target:
                return 
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                dfs(i+1, total + nums[i])
                path.pop()
                
        dfs(0, 0)
        return ans