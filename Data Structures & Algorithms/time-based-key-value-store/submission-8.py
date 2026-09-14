class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print(f"Set {key} {timestamp}")
        d = self.d
        if key not in d:
            d[key] = [(timestamp, value)]
        else:
            d[key].append((timestamp, value))

        

    def get(self, key: str, t: int) -> str:
        # print(f"get {key} {timestamp}")
        d = self.d
        if key not in d:
            return ""

        a = d[key]
        if a[0][0] > t:
            return ""

        # find first equal or smaller 
        n = len(a)
        # print(a)
        l, r = 0, n - 1 
        while l <= r:
            m = (l + r) // 2
            # print (l,r,m)
            if a[m][0] == t:
                return a[m][1]
            elif a[m][0] < t:
                l = m + 1
            else: 
                r = m - 1   
        return a[l-1][1]
