class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = {}
        end = {}
        output = 0
        # end = start + length
        for num in nums:
            start[num] = 1
            end[num] = 1
            output = 1
        for num in nums:
            # 恰好把2段合为1段
            if num + 1 in start and num - 1 in end:
                new_end = num + start[num + 1]
                new_start = num - end[num - 1]
                new_length = new_end - new_start + 1
                start[new_start] = new_length
                end[new_end] = new_length
                output = max(output, new_length)
            # 在段左边
            if num + 1 in start:
                start[num] = start[num + 1] + 1 
                end[num + start[num + 1]] = start[num] 
                output = max(output, start[num])
            # 在段右边
            if num - 1 in end:
                end[num] = end[num - 1] + 1
                start[num - end[num - 1]] = end[num]
                output = max(output, end[num])

        for num in nums:
            # 恰好把2段合为1段
            if num + 1 in start and num - 1 in end:
                new_end = num + start[num + 1]
                new_start = num - end[num - 1]
                new_length = new_end - new_start + 1
                start[new_start] = new_length
                end[new_end] = new_length
                output = max(output, new_length)
            # 在段左边
            if num + 1 in start:
                start[num] = start[num + 1] + 1 
                end[num + start[num + 1]] = start[num] 
                output = max(output, start[num])
            # 在段右边
            if num - 1 in end:
                end[num] = end[num - 1] + 1
                start[num - end[num - 1]] = end[num]
                output = max(output, end[num])
        
        for num in nums:
            # 恰好把2段合为1段
            if num + 1 in start and num - 1 in end:
                new_end = num + start[num + 1]
                new_start = num - end[num - 1]
                new_length = new_end - new_start + 1
                start[new_start] = new_length
                end[new_end] = new_length
                output = max(output, new_length)
            # 在段左边
            if num + 1 in start:
                start[num] = start[num + 1] + 1 
                end[num + start[num + 1]] = start[num] 
                output = max(output, start[num])
            # 在段右边
            if num - 1 in end:
                end[num] = end[num - 1] + 1
                start[num - end[num - 1]] = end[num]
                output = max(output, end[num])
        for num in nums:
            # 恰好把2段合为1段
            if num + 1 in start and num - 1 in end:
                new_end = num + start[num + 1]
                new_start = num - end[num - 1]
                new_length = new_end - new_start + 1
                start[new_start] = new_length
                end[new_end] = new_length
                output = max(output, new_length)
            # 在段左边
            if num + 1 in start:
                start[num] = start[num + 1] + 1 
                end[num + start[num + 1]] = start[num] 
                output = max(output, start[num])
            # 在段右边
            if num - 1 in end:
                end[num] = end[num - 1] + 1
                start[num - end[num - 1]] = end[num]
                output = max(output, end[num])
        return output
            
        