class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for i in tasks:
            d[i] += 1
        cnt_tasks = []
        for k,v in d.items():
            cnt_tasks.append((-v, k))
        heapq.heapify(cnt_tasks) 
        arragement = []
        reserve = {}
        far = {}
        cur = max_far = 0
        q = deque()
        q_d = {}
        while len(cnt_tasks) > 0:
            if cur in reserve:
                q.append(task)
                if len(q) > n:
                    left = q.popleft()
                    q_d.pop(left, None)
                q_d[task] = cur
                cur += 1
                continue
            # pick cnt biggest one and put it back 
            cnt_task = heapq.heappop(cnt_tasks)
            task = cnt_task[1]
            new_cnt = cnt_task[0] + 1
            if new_cnt < 0:
                cnt_task = (new_cnt, cnt_task[1])
                heapq.heappush(cnt_tasks, cnt_task)
            
            if task in q_d:
                if task not in far:
                    far[task] = q_d[task]
                far[task] += (1 + n)
                max_far = max(max_far, far[task])
                reserve[far[task]] = task
            else:
                q.append(task)
                if len(q) > n:
                    left = q.popleft()
                    q_d.pop(left, None)
                q_d[task] = cur
                cur += 1
        return max(cur, max_far + 1)
            