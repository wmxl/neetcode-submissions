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
                
        print(d)
        
        def dd(n: int) -> int:
            if d[n] == n:
                return n
            if d[n] in d:
                return dd(d[n])
            return d[n]


        for i, num in enumerate(nums):
            mi = dd(num)
            output = max(output, num - mi + 1)
            
        return output
            
        