class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        i = 0
        while True:
            i += 1 
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        slow = fast = 0
        while i > 0:
            fast = nums[fast]
            i -= 1
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow
        