class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x * x + y * y

        ksmall = []
        distance2point = {}
        tiny = 0.00000000001
        for point in points:
            dist = -distance(point[0], point[1])
            if dist in distance2point:
                dist += tiny
                tiny += 0.00000000001
            distance2point[dist] = [point[0], point[1]]
            if len(ksmall) < k:
                heapq.heappush(ksmall, dist)
            else:
                heapq.heappush(ksmall, dist)
                should_remove = heapq.heappop(ksmall)

                # distance2point.pop(should_remove, None)
                del distance2point[should_remove]
        return [distance2point[i] for i in ksmall]
        

        
            