class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        print(stones)
        stones = [-i for i in stones]
        heapq.heapify(stones)

        
        while len(stones) > 1:
            max_one = -heapq.heappop(stones)
            max_two = -heapq.heappop(stones)
            left = max_one - max_two
            
            heapq.heappush(stones, -left)
        
        return -stones[0]