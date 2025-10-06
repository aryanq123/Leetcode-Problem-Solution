    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        for i in range(n):
            for j in range(i+1,n):
                tmp=prices[j]-prices[i]
                if profit <tmp and tmp > 0:
                    profit=tmp
        return profit
