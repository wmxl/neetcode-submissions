class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        n = len(s)
        def ispalindrome(s):
            for i in range(len(s)):
                if s[i] != s[-1-i]:
                    return False
            return True

        def dfs(s, start, end, ans):
            if end == len(s) + 1:
                print(start, end, ans)
                if start == end - 1:
                    output.append(ans)
                return

            if ispalindrome(s[start:end]):
                # print(f"palindrome: {start}:{end} {s[start:end]}")
                ans2 = ans[:]
                ans2.append(s[start:end])
                dfs(s, end, end+1, ans2)

            dfs(s, start, end+1, ans[:])

        dfs(s, 0, 1, [])
        return output