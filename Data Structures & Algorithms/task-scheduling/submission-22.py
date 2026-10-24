class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for i in tasks:
            d[i] += 1
        cnt_tasks = []
        for k,v in d.items():
            cnt_tasks.append((-v, k))
        heapq.heapify(cnt_tasks) 
        # print(cnt_tasks)

        arragement = []
        reserve = {}
        far = {}
        cur = max_far = 0
        while len(cnt_tasks) > 0:
            if cur in reserve:
                arragement.append(reserve[cur])
                cur += 1
                continue

            # pick cnt biggest one and put it back 
            cnt_task = heapq.heappop(cnt_tasks)
            # print(cnt_task)
            task = cnt_task[1]
            new_cnt = cnt_task[0] + 1
            if new_cnt < 0:
                cnt_task = (new_cnt, cnt_task[1])
                heapq.heappush(cnt_tasks, cnt_task)
            # print(cnt_tasks)
            
            j = cur - 1
            same = False
            while j >= 0 and j >= cur - n:
                if task == arragement[j]:
                    if task not in far:
                        far[task] = j
                    far[task] += (1 + n)
                    # print(f"far {task} {far[task]}")
                    max_far = max(max_far, far[task])
                    reserve[far[task]] = task
                    same = True
                    break
                else:
                    j -= 1

            if not same:
                arragement.append(task)
                cur += 1
            # print(cnt_tasks)

        # print(arragement)
        
        return max(cur, max_far + 1)
            