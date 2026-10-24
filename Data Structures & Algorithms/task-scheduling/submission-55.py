class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        highest = 0
        for i in tasks:
            d[i] += 1
            highest = max(highest, d[i])

        num = sum([1 for v in d.values() if v == highest])
        
        remain = len(tasks) - highest * num
        empty = (n - num + 1) * (highest - 1)
        if empty > remain:
            ans = empty + highest * num
        else:
            ans = len(tasks)

        return ans