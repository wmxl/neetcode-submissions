class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        s = []
        def dfs(i, left, right):
            print(i, left, right)
            if i >= 2 * n:
                ans.append("".join(s))
                # print(ans)
                return
                
            if left < n:
                s.append('(')
                dfs(i+1, left+1, right)
                s.pop()
            if right < left:
                s.append(')')
                dfs(i+1, left, right+1)
                s.pop()

        dfs(0,0,0)
        return ans
