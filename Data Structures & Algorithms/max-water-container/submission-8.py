class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)
        if n <= 1:
            return 0

        def area(i, j):
            return min(h[i],h[j]) * (j - i)

        i = 0
        j = n - 1
        best = area(i, j)
        while i < j:
            if min(h[i], h[j-1]) > min(h[i],h[j]):
                best = max(best, area(i,j-1))
                j -= 1
                continue
            elif min(h[i+1], h[j]) > min(h[i],h[j]):
                best = max(best, area(i+1,j))
                i += 1
                continue

            left = h[i] 
            right = h[j]

            if left <= right:
                flag = False
                while i < j and h[i + 1] <= left:
                    i += 1
                    flag = True
                    break
                if flag:
                    continue
            else:                
                flag = False
                while i < j and h[j-1] <= right:
                    j -= 1
                    flag = True
                    break
                if flag:
                    continue

            i += 1

        return best
    