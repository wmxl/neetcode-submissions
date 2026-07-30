class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = num
        

        for i, num in enumerate(nums):
            if num - 1 in d:
                d[num] = d[num - 1] 
            if num + 1 in d:
                d[num + 1] = d[num]

        for i, num in enumerate(nums):
            if num - 1 in d:
                d[num] = d[num - 1] 
            if num + 1 in d:
                d[num + 1] = d[num]

        print(d)
        for i, num in enumerate(nums):
            output = max(output, num - d[num] + 1)
            
        return output
            
        