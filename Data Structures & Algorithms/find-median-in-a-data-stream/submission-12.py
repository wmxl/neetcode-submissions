class max_heapq:
    def heappush(q, e):
        return heapq.heappush(q, -e)

    def heappop(q):
        return -heapq.heappop(q)

    def heappushpop(q, e):
        max_heapq.heappush(q, e)
        return max_heapq.heappop(q)


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
                max_heapq.heappush(small, num)
            else:
                max_heapq.heappush(small, big[0])
                heapq.heappushpop(big, num)
        else:
            if num > -small[0]:
                heapq.heappush(big, num)
            else:
                heapq.heappush(big, -small[0])
                max_heapq.heappushpop(small, num)
        

    def findMedian(self) -> float:
        small = self.small
        big = self.big

        if not small and not big:
            return 0
        elif len(big) > len(small):
            return big[0]            
        else:
            return (big[0] - small[0]) / 2
        
        