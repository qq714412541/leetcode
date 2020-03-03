class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        i = 1
        init = prices[0]
        while i <= len(prices):
            if i == len(prices):
                return 0
            if prices[i] < init:
                init = prices[i]
                i += 1
            else:
                break
        cur_low = prices[i - 1]
        temp = prices[i - 1]
        cur_high = prices[i]
        max_pro = cur_high - cur_low

        for j in range(i + 1, len(prices)):
            cur_max = prices[j] - cur_low
            max_pro = max(max_pro, cur_max)
            # print(max_pro)
            if prices[j] - temp > max_pro:
                max_pro = prices[j] - temp
                # print(max_pro,temp)
                cur_low = temp
            else:
                if prices[j] < temp:
                    temp = prices[j]
                else:
                    continue
        return max_pro

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pri,max_pro = float('inf'),0
        for price in prices:
            min_pri = min(min_pri,price)
            cur_pro = price - min_pri
            max_pro = max(max_pro,cur_pro)
        return max_pro