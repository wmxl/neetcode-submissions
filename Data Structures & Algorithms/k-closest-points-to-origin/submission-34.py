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
                if len(distance2point[should_remove]) > 1:
                    distance2point[should_remove].pop()
                else:
                    distance2point.pop(should_remove)

        count = {}
        ans = []
        for item in ksmall:
            count[item] = count.get(item, -1) + 1
            ans.append(distance2point[item][count[item]])
                
        return ans
        

        
            