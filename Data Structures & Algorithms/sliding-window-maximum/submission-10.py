class Solution:
    def maxSlidingWindow(self, a: List[int], k: int) -> List[int]:
        n = len(a)
        j = 0
        q = deque() # store index of element
        output = []
        while j < n:
            cur = a[j]
            while q and a[q[-1]] <= cur:
                q.pop()
            q.append(j)

            i = j - k + 1 
            if i >= 0:
                output.append(a[q[0]])
                if i == q[0]:
                    q.popleft()
            j += 1
        
        return output
