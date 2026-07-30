class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        d = {}
        ns= []
        start = {}
        for i, num in enumerate(nums):
            if num in d:
                continue
            d[num] = num
            ns.append(num)
        
        print(ns)
        
        for num in ns:
            if num - 1 not in d:
                start[num] = 1
        
        for k,v in start.items():
            nx = k + 1
            while True:
                if nx in d:
                    start[k] += 1
                    nx += 1
                else:
                    break
            output = max(output, start[k])
        print(start)    

        return output
            
        