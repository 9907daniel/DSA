class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        a = []
        l = 0
        r = 1
        current_max = 0

        if len(prices) > 3:
            while l < len(prices)-2:
                for r in prices[r:]:
                    if r > prices[l]:
                        current_max = max(current_max,r-prices[l])
                l += 1
                r = l+1
            
            return current_max
        else:
            if len(prices) == 1:
                return 0
            elif prices[r]-prices[l]>0:
                return prices[r]-prices[l]
            else:
                return 0



        
        # while first < len(prices)-1:
        #     for second in range(first+1, len(prices)-1):
        #         if prices[first] < prices[second+1]:
        #             if len(l) == 0:
        #                 l.append(prices[second]-prices[first])
        #                 second += 1
        #             elif prices[second]-prices[first] > l[0] and second < len(prices):
        #                 l.pop()
        #                 l.append(prices[second]-prices[first])
        #                 second += 1
        #         else:
        #             second += 1
        #         second = first +1
        #     first += 1
        
        # if len(l) == 0:
        #     return 0
        # else: 
        #     return l[0]

                    
            



        # if prices.index(min(prices)) != len(prices)-1:
        #     buy = prices.index(min(prices))
        # else:
        
        # after_buy_prices = prices[buy+1:]

        # sell = prices.index(max(after_buy+prices, default=min(prices)))
        # # print(sell)

        # if prices[buy] > prices[sell] or prices[buy]==prices[-1]:
        #     return 0
        # else:
        #     return prices[sell]-prices[buy]
