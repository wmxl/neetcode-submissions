class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ma = 0
        for i in range(n):
            j = i
            d = {}
            cnt = 0
            while j < n:
                if s[j] in d: 
                    break
                d[s[j]] = 1
                cnt += 1
                j += 1
            ma = max(ma, cnt)
        return ma
                
