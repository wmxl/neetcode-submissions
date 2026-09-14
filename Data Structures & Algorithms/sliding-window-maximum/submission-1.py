class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        def remove(x: int):
            deleted[x] += 1

        def top():
            while h and deleted[h[0]] > 0:
                deleted[h[0]] -= 1
                heapq.heappop(h)
            return h[0] if h else None

        n = len(a)
        i, j = 0, k-1
        output, h = [], []
        deleted = Counter()

        a = [-i for i in a]
        h = a[:k]
        heapq.heapify(h)

        while j < n:
            num = top()
            output.append(-num)
            remove(a[i])
            i += 1
            j += 1
            if j >= n:
                break
            heapq.heappush(h, a[j])

        return output