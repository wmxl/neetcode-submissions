class Solution:
    def search(self, a: List[int], t: int) -> int:
        n = len(a)
        i, j  = 0, n-1
        while i <= j:
            m = (i + j) // 2
            if a[m] == t:
                return m
            elif a[m] <= a[j]:
                if a[m] < t <= a[j]:
                    i = m + 1
                else:
                    j = m - 1
            else:
                if a[j] < t < a[m]:
                    j = m - 1
                else:
                    i = m + 1
        return -1
                