class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        i, j = 0, 0
        q = deque() # store index of element
        while j < k - 1:
            cur = a[j]
            while q and a[q[-1]] <= cur:
                q.pop()
            q.append(j)
            j += 1
        
        # j from k-1
        output = []
        while j < n:
            cur = a[j]
            while q and a[q[-1]] <= cur:
                q.pop()
            q.append(j)

            output.append(a[q[0]])

            if j-k+1 == q[0]:
                q.popleft()

            j += 1

        return output
