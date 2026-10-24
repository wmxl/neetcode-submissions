class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        klarge = []
        for i in nums:
            if len(klarge) < k:
                heapq.heappush(klarge, i)
            else:
                heapq.heappushpop(klarge, i)
        return klarge[0]