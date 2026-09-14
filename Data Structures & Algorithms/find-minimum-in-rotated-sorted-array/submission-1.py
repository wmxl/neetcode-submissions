class Solution:
    def findMin(self, a: List[int]) -> int:
        n = len(a)
        if n < 2:
            return a[0]
        i, j = 0, n-1
        while i <= j:
            m = (i + j) // 2
            print(f"{i} {j} {m}")
            if m == i:
                return min(a[i], a[j])
            if a[m-1] > a[m] < a[m+1]:
                return a[m]
            elif a[m] < a[i] and a[m] < a[j]:
                j = m - 1
            elif a[m] > a[i] and a[m] > a[j]:
                i = m + 1
            elif a[i] < a[m] and a[m] < a[j]:
                return a[i]
            else:
                print(f"else {i} {j} {m}")
        # print(f"else {i} {j} {m}")
        return a[m]