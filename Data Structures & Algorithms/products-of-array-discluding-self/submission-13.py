class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d = {}
        d[(-1, -1)] = 1
        d[(n, n)] = 1
        for i in range(0, n - 1):
            key = (-1, i) #  (-1, 0) ~ (-1, n - 2)
            pre_key = (-1, i - 1)
            d[key] = d[pre_key] * nums[i]

        for i in range(1, n):
            key = (n - i, n) # (1, n) ~ (n - 1, n)
            pre_key = (n - i + 1, n)
            d[key] = d[pre_key] * nums[n - i]

        output = []
        for i in range(0, n):
            output.append(d[(-1, i - 1)] * d[(i + 1, n)])
        return output
        