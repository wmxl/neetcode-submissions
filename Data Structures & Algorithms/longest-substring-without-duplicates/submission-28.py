class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        i = ma = 0
        for j, c in enumerate(s):
            if c in last and last[c] >= i:
                i = last[c] + 1
            last[c] = j
            ma = max(ma, j - i + 1)
        return ma