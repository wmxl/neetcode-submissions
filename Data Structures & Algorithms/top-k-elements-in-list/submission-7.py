from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1    

        sorted_items = sorted(cnt.items(), key = lambda x: x[1], reverse = True)

        res = []
        for i, item in enumerate(sorted_items):
            res.append(item[0])
            if i >= k-1:
                return res
        return res

