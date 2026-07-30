class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a.sort()
        res = []
        for k, num in enumerate(a):
            if k - 1 >= 0 and a[k] == a[k - 1]:
                continue
            i = k + 1
            j = len(a) - 1
            while i < j:
                if a[i] + a[j] == -num:
                    res.append([num, a[i], a[j]])
                    i += 1
                    j -= 1
                    while i < j and a[i] == a[i - 1]:
                        i += 1
                    while i < j and a[j] == a[j + 1]:
                        j -= 1

                elif a[i] + a[j] > -num:
                    j -= 1
                elif a[i] + a[j] < -num:
                    i += 1
        return res