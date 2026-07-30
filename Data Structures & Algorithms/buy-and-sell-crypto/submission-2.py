class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        n = len(p)
        if n == 0: return 0
        mi = p[0]
        profit = 0
        for i in p:
            if i < mi:
                mi = i
            if i > mi:
                profit = max(profit,i - mi)
        return profit
            

        