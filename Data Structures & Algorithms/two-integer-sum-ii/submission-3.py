class Solution:
    def twoSum(self, a: List[int], target: int) -> List[int]:
        j = len(a) - 1
        i = 0
        while i < j:
            if a[i] + a[j] == target:
                return [i+1,j+1]
            elif a[i] + a[j] > target:
                j -= 1
            elif a[i] + a[j] < target:
                i += 1
        return [i+1,j+1]


        