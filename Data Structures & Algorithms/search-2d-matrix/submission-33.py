class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        
        def search(nums: List[int], t: int) -> int:
            n = len(nums)
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == t:
                    return True
                elif nums[m] > t:
                    r = m - 1
                else:
                    l = m + 1
            return False

        # firstly confirm which row
        a = []
        for row in matrix:
            a.append(row[0])
        a.append(matrix[-1][-1])
        print(a)

        n = len(a)
        l = 0
        r = n - 1
        possible = -1
        while l <= r:
            m = (l + r) // 2
            print(f'{l} {r} {m}')
            if a[m] == t:
                return True
            elif a[m] > t:
                if  m-1 > 0 and t > a[m-1]:
                    print(f"serach m-1 {m-1}")
                    return search(matrix[m-1], t)
                r = m - 1
            else:
                if  m+1 < n and t < a[m+1] :
                    print(f"serach m {m}")
                    return search(matrix[m], t)
                l = m + 1

        return False