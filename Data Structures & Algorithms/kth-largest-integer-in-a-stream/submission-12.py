class KthLargest:
    klarge = []
    k = 0
    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse = True)
        self.klarge = nums[0:k]
        self.k = k


    def add(self, val: int) -> int:
        klarge = self.klarge
        if len(klarge) < self.k:
            klarge.append(val)
            klarge.sort(reverse = True)
            return klarge[-1]
        if val <= klarge[-1]:
            return klarge[-1]
        klarge.append(val)
        klarge.sort(reverse = True)
        klarge.pop()
        return klarge[-1]


        
