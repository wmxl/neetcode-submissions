class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0]) 


        l = 0
        r = n*m - 1
        while l <= r:
            mid = (l + r) // 2

            i = mid // n
            j = mid % n 
            cur = matrix[i][j]

            if cur == t:
                return True
            elif cur > t:
                r = mid - 1
            else:
                l = mid + 1
        return False