class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x * x + y * y

        ksmall = []
        for point in points:
            dist = -distance(point[0], point[1])
            if len(ksmall) < k:
                heapq.heappush(ksmall, (dist, [point[0], point[1]]))
            else:
                heapq.heappushpop(ksmall, (dist, [point[0], point[1]]))
                
        return [i[1] for i in ksmall]
        

        
            