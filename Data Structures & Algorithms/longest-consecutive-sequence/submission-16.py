class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = {}
        end = {}
        output = 0
        for num in nums:
            if num in start or num in end:
                continue
            # 恰好把2段合为1段
            if num + 1 in start and num - 1 in end:
                new_end = num + start[num + 1]
                
                print(f'start[{num+1}]= {start[num+1]}')
                new_start = num - end[num - 1]
                new_length = new_end - new_start + 1
                start[new_start] = new_length
                end[new_end] = new_length
                output = max(output, new_length)
                print(f'2段合为1 {new_start}-{new_end}:{new_length}')     
                continue
            # 在段左边
            if num + 1 in start:
                start[num] = start[num + 1] + 1 
                end[num + start[num + 1]] = start[num] 
                output = max(output, start[num])
                print(f'在段左边 {num}-{num + start[num + 1]}:{start[num]}')
                continue
            # 在段右边
            if num - 1 in end:
                end[num] = end[num - 1] + 1
                start[num - end[num - 1]] = end[num]
                output = max(output, end[num])
                print(f'end[{num-1}]={end[num-1]}')
                print(f'end[{num}]={end[num]}')
                print(f'在段右边 {num - end[num - 1]}-{num}:{end[num]}')
                continue
            start[num] = 1
            end[num] = 1
            output = max(output, 1)
            

        return output
            
        