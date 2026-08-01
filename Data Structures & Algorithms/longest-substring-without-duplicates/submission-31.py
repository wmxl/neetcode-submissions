class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = ma = 0
        d = {}
        i = j = 0
        while j < n:
            if s[j] in d and d[s[j]] >= i: 
                # print(f'repeat:{repeat} i:{i} j:{j}')
                i = d[s[j]] + 1
                d[s[j]] = j

            else:
                d[s[j]] = j
                ma = max(ma, j - i + 1)

            j += 1            

        return ma
                
