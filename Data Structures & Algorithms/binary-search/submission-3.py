class Solution:
    def search(self, nums: List[int], t: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == t:
                return m
            elif nums[m] > t:
                r = m - 1
            else:
                l = m + 1
        return -1
        