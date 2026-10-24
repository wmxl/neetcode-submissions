class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        highest = 0
        for i in tasks:
            d[i] += 1
        cnt_tasks = []
        for k, v in d.items():
            cnt_tasks.append((-v, k))
        heapq.heapify(cnt_tasks) 

        highest = cnt_tasks[0][0]
        num = 0
        while cnt_tasks and cnt_tasks[0][0] == highest:
            heapq.heappop(cnt_tasks)
            num += 1
        
        highest = -highest
        remain = len(tasks) - highest * num
        empty = (n - num + 1) * (highest - 1)
        if empty > remain:
            ans = empty + highest * num
        else:
            ans = len(tasks)

        return ans