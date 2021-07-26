#输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

# class Solution:
#     def maxProfit(self, prices) -> int:
#         i = 0
#         profit = 0
#         while len(prices) > 0:
#             if len(prices) > 1:
#                 if prices[i] < prices[i+1]:
#                     profit += prices[i+1] - prices[i]
#                     prices.remove(prices[i])
#                     prices.remove(prices[i+1])
#                 else:
#                     prices.remove(prices[i])
#             else:
#                 break
#         return profit

class Solution:
    def maxProfit(self, prices) -> int:
        i = 0
        profit = 0
        temp_list = []
        while len(prices) > 1:
            if prices[i] > prices[i+1]:
                prices.remove(prices[i])
            else:
                for j in range(0,len(prices)-1):
                    if prices[j+1] >= prices[j]:
                        temp_list.append(prices[j+1])
                    else:
                        break
                profit += max(temp_list) - prices[i]
                prices.remove(prices[i])
                for k in temp_list:
                    prices.remove(k)
                temp_list = []
        return profit

# [7,1,5,3,6,4] [1,5,3,6,4] [3,6,4] [4]
# [1,2,3,4,5] [2,3,4,5]
# [7,6,4,3,1] [6,4,3,1] [4,3,1] [3,1] [1]


print(Solution.maxProfit(self='self',prices=[3,3]))
