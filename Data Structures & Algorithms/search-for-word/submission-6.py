class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            # print(f'dfs {i} {j} {k}')
            if i < 0 or j < 0 or i >= m or j >= n: return
            if v[i][j]: return

            x = board[i][j]
            v[i][j] = True
            if x == word[k]:
                # print(f'dfs  {i} {j} {x} {k}')
                if k == len(word) - 1:
                    nonlocal ans
                    ans = True
                    # print(True)
                    return 
                dfs(i, j+1, k+1)
                dfs(i+1, j, k+1)
                dfs(i-1, j, k+1)
                dfs(i, j-1, k+1)
            v[i][j] = False

        ans = False
        m, n = len(board), len(board[0])
        v = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
        return ans
        