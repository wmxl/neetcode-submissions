class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.klarge = nums[0:k]
        self.k = k
        heapq.heapify(self.klarge) 


    def add(self, val: int) -> int:
        klarge = self.klarge

        if len(klarge) < self.k:
            heapq.heappush(klarge, val)
            return klarge[0]

        if val >= klarge[0]:
            heapq.heappushpop(klarge, val)
        
        return klarge[0]


        
