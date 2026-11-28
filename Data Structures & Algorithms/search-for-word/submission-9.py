class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= m or j >= n: return False
            if v[i][j]: return False

            x = board[i][j]
            v[i][j] = True
            res = False
            if x == word[k]:
                if k == len(word) - 1:
                    return True
                res = dfs(i, j+1, k+1) or dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
                
            v[i][j] = False
            return res

        m, n = len(board), len(board[0])
        v = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
        