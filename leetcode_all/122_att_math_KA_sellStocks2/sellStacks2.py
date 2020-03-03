class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        is_min = False
        is_max = False
        profit = 0
        while i <= len(prices) - 1:

            while i <= len(prices) - 1 and not is_min:
                is_min = self.is_min(prices, i)
                i += 1
                cur_low = prices[i - 1]
            if i == len(prices):
                break
            is_min = False

            while i <= len(prices) - 1 and not is_max:
                is_max = self.is_max(prices, i)
                i += 1
                cur_high = prices[i - 1]
            is_max = False

            profit += (cur_high - cur_low)
            # print(profit)
        return profit

    def is_max(self, arr, i):
        if i == len(arr) - 1:
            return True

        if arr[i - 1] <= arr[i] and arr[i + 1] <= arr[i]:
            return True
        else:
            return False

    def is_min(self, arr, i):
        # print(i,i+1,i-1)
        if i == len(arr) - 1:
            return True
        if i == 0 and arr[i] <= arr[i + 1]:
            return True
        if arr[i + 1] >= arr[i] and arr[i - 1] >= arr[i]:
            return True
        else:
            return False


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=(prices[i+1]-prices[i])
        return profit


