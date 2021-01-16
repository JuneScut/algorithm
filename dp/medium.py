# 714 股票交易 
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 因此每天存在两种状态：持有股票或者不持有股票
# 注意到在状态转移方程中，\textit{dp}[i][0]dp[i][0] 和 \textit{dp}[i][1]dp[i][1] 只会从 \textit{dp}[i-1][0]dp[i−1][0] 和 \textit{dp}[i-1][1]dp[i−1][1] 转移而来，因此我们不必使用数组存储所有的状态，而是使用两个变量 \textit{sell}sell 以及 \textit{buy}buy 分别表示 \textit{dp}[..][0]dp[..][0] 和 \textit{dp}[..][1]dp[..][1] 直接进行状态转移即可。

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        days = len(prices)
        if days == 0:
            return 0
        profit = [[0 for _ in range(0, 2)] for _ in range(0, days)]
        profit[0][0] = 0
        profit[0][1] = -prices[0]
        for index in range(1, days):
            profit[index][0] = max(profit[index-1][0], profit[index-1][1] + prices[index] - fee)
            profit[index][1] = max(profit[index-1][0] - prices[index], profit[index-1][1])
        return profit[days-1][0]


solution = Solution()
print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))