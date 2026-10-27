class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        small = self.small
        big = self.big

        if not small and not big:
            big.append(num)
        elif len(big) > len(small):
            if num < big[0]:
                heapq.heappush(small, -num)
            else:
                heapq.heappush(small, -big[0])
                heapq.heappushpop(big, num)
        else:
            if num > -small[0]:
                heapq.heappush(big, num)
            else:
                heapq.heappush(big, -small[0])
                heapq.heappushpop(small, -num)
        

    def findMedian(self) -> float:
        small = self.small
        big = self.big

        if not small and not big:
            return 0
        elif len(big) > len(small):
            return big[0]            
        else:
            return (big[0] - small[0]) / 2
        
        