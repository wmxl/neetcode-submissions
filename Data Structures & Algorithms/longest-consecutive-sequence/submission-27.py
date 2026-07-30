class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        d = {}
        e = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = num
                e[num] = num
        
        for i, num in enumerate(nums):
            if num - 1 in d:
                d[num] = d[num - 1] 
                e[num - 1] = num


                if num in e:
                    d[e[num]] = d[num - 1] 
            if num + 1 in d:
                d[num + 1] = d[num]
                e[num] = e[num + 1]

                if num + 1 in e:
                    d[e[num + 1]] = d[num] 



        print(d)
        for i, num in enumerate(nums):
            output = max(output, num - d[num] + 1)
            
        return output
            
        