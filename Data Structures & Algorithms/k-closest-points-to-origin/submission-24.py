class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return x * x + y * y

        ksmall = []
        distance2point = {}
        multi = {}
        tiny = 0.00000000001
        for point in points:
            dist = -distance(point[0], point[1])
            if dist in distance2point:
                distance2point[dist].append([point[0], point[1]]) 
            else:
                distance2point[dist] = [[point[0], point[1]]]
            if len(ksmall) < k:
                heapq.heappush(ksmall, dist)
            else:
                heapq.heappush(ksmall, dist)
                should_remove = heapq.heappop(ksmall)
                if should_remove in distance2point and distance2point[should_remove] and len(distance2point[should_remove]) > 1:
                    distance2point[should_remove].pop()

                distance2point.pop(should_remove, None)

        count = {}
        ans = []
        for item in ksmall:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
            ans.append(distance2point[item][count[item]-1])
                
        return ans
        

        
            