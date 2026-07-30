class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        d[(0, 0)] = nums[0]
        d[(n - 1, n - 1)] = nums[n - 1]
        d[(0, -1)] = 1
        d[(n, n-1)] = 1
        for i in range(1, n - 1):
            key = (0, i) #  (0, 1) ~ (0, n - 2)
            pre_key = (0, i - 1)
            d[key] = d[pre_key] * nums[i]

        for i in range(2, n):
            key = (n - i, n - 1) # (1, n - 1) ~ (n - 2, n - 1)
            pre_key = (n - i + 1, n - 1)
            d[key] = d[pre_key] * nums[n - i]

        output = []
        for i in range(n):
            output.append(d[(0, i - 1)] * d[(i + 1, n - 1)])
        return output
        