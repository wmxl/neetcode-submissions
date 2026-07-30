class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        a = sorted(a)
        print(a)
        res = []
        for k, num in enumerate(a):
            if k - 1 >= 0 and a[k] == a[k - 1]:
                continue
            print(f"k = {k}")
            i = 0
            j = len(a) - 1
            while i < j:
                if i == k:
                    i += 1
                    continue
                if j == k:
                    j -= 1
                    continue
                if a[i] + a[j] == -num:
                    print(num, a[i], a[j])
                    if num <= a[i]:
                        res.append([num, a[i], a[j]])
                    elif num <= a[j]:
                        res.append([a[i], num, a[j]])
                    else:
                        res.append([a[i], a[j], num])
                    i += 1
                    j -= 1
                elif a[i] + a[j] > -num:
                    j -= 1
                elif a[i] + a[j] < -num:
                    i += 1

        ss = set()
        for x in res:
            ss.add(tuple(x))
        print(ss)
        res = list(ss)
        return res