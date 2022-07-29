# !/usr/bin/env python3
# coding=utf-8
import collections
from math import log2
from typing import List


# 714 股票交易
# 如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 因此每天存在两种状态：持有股票或者不持有股票
# 注意到在状态转移方程中，\textit{dp}[i][0]dp[i][0] 和 \textit{dp}[i][1]dp[i][1] 只会从 \textit{dp}[i-1][0]dp[i−1][0] 和 \textit{dp}[i-1][1]dp[i−1][1] 转移而来，因此我们不必使用数组存储所有的状态，而是使用两个变量 \textit{sell}sell 以及 \textit{buy}buy 分别表示 \textit{dp}[..][0]dp[..][0] 和 \textit{dp}[..][1]dp[..][1] 直接进行状态转移即可。

# class Solution(object):
#     def maxProfit(self, prices, fee):
#         """
#         :type prices: List[int]
#         :type fee: int
#         :rtype: int
#         """
#         days = len(prices)
#         if days == 0:
#             return 0
#         profit = [[0 for _ in range(0, 2)] for _ in range(0, days)]
#         profit[0][0] = 0
#         profit[0][1] = -prices[0]
#         for index in range(1, days):
#             profit[index][0] = max(profit[index-1][0], profit[index-1][1] + prices[index] - fee)
#             profit[index][1] = max(profit[index-1][0] - prices[index], profit[index-1][1])
#         return profit[days-1][0]


# solution = Solution()
# print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))

# 【300】[最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)
# ① 子序列不一定是连续的，子串才是连续的
# ② dp(n) 的定义：最长下标为 n 的字符串的最长递增子序列的长度
# ③ 最优子结构：最长下标为 n 的字符串的最长递增子序列的长度 = 找到子序列的最后一个数字小于 nums[n], 把它 +1，这个子序列找长度最长的
# ④ base case: dp(0) = 1

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums or len(nums) == 0:
#             return 0
#         dpArr = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#                 if nums[i] > nums[j]:
#                     dpArr[i] = max(dpArr[i], dpArr[j] + 1)
#         # 在这个dp数组里找最大值
#         lst = dpArr[0]
#         for i in dpArr:
#             if i > lst:
#                 lst = i
#         return lst


# solution = Solution()
# print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7]))

# 【1143】[最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)
# 先从递归，再换成迭代
# text1 = "abcde", text2 = "ace"， lcs = ace
# ① dp 定义：dp[i][j] 表示 text1[0...i]和 text2[0...j] 的最长公共子序列
# ② 最优子结构：考虑处理每一个字符：
#       text1[i] == text2[j] 时，dp[i][j] = 1 + dp[i-1] + dp[j-1]
#       text1[i] != text2[j] 时，text1[i] 和 text2[j] 至少有一个不在 lcs 中
#           可能 text1[i] 不在 lcs 中：dp[i][j] = dp[i-1][j]
#           可能 text2[j] 不在 lcs 中：dp[i][j] =  dp[i][j-1]
#
# ③ base case: i == len(text1) or j == len(text2)
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m = len(text1) + 1
#         n = len(text2) + 1
#         dp = [[0] * n for _ in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 # 因为是从 1 开始，所以需要 -1
#                 if text1[i-1] == text2[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#         return dp[m-1][n-1]


# solution = Solution()
# print(solution.longestCommonSubsequence("abcba", "abcbcba"))

# 【583】[两个字符串的删除操作](https://leetcode-cn.com/problems/delete-operation-for-two-strings/)
# class Solution:
#     def longestCommonSubsequence(self, s1: str, s2: str) -> int:
#         m, n = len(s1) + 1, len(s2) + 1
#         dp = [[0] * n for _ in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 if s1[i-1] == s2[j-1]:
#                     dp[i][j] = 1 + dp[i-1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i][j-1], dp[i-1][j])
#         return dp[m-1][n-1]

#     def minDistance(self, word1: str, word2: str) -> int:
#         lcs = self.longestCommonSubsequence(word1, word2)
#         return len(word1) - lcs + len(word2) - lcs


# solution = Solution()
# print(solution.minDistance("", ""))

# 【712】[两个字符串的最小 ASCII 删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/)
# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         m, n = len(s1), len(s2)
#         # memo[i][j] 表示 s1[0...i][0..j] 的最小 ASCII 删除和
#         memo = [[-1] * n for _ in range(m)]

#         def dp(i, j) -> int:
#             res = 0
#             # base case
#             if i == m:
#                 for item in range(j, n):
#                     res += ord(s2[item])
#                 return res
#             if j == n:
#                 for item in range(i, m):
#                     res += ord(s1[item])
#                 return res
#             if memo[i][j] != -1:
#                 return memo[i][j]
#             if s1[i] == s2[j]:
#                 memo[i][j] = dp(i+1, j+1)
#             else:
#                 memo[i][j] = min(ord(s1[i]) + dp(i+1, j),
#                                  ord(s2[j]) + dp(i, j+1))
#             return memo[i][j]

#         return dp(0, 0)


# solution = Solution()
# print(solution.minimumDeleteSum("", ""))


# 【64】[最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)
# 🐱 二维动态规划
# dp[i][j] 表示从 grid[0][0] 到 grid[i][j] 的最小路径和
# 最优子结构： dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
# base case: dp[0][j] 和 dp[i][0]
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         rows = len(grid)
#         columns = len(grid[0])
#         if rows == 0 or columns == 0:
#             return 0
#         dp = [[0] * columns for _ in range(rows)]
#         # base case
#         dp[0][0] = grid[0][0]
#         for j in range(1, columns):
#             dp[0][j] = dp[0][j-1] + grid[0][j]
#         for i in range(1, rows):
#             dp[i][0] = dp[i-1][0] + grid[i][0]
#         # 最优子结构
#         for i in range(1, rows):
#             for j in range(1, columns):
#                 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#         return dp[rows-1][columns-1]


# solution = Solution()
# print(solution.minPathSum([[1, 2, 3], [4, 5, 6]]))


# 【416】[分隔等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
# 背包问题，有 n 个物品 nums, 背包重量恰好为 sums(nums) / 2
# 状态：i 个物品，背包重量 j
# dp[i][j] 定义：前 i 个物品，是否能装满重量为 j, base case: dp[0][...] = 0, dp[...][0] = 1
# 转移：dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
# 一维压缩, TODO:
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         total = sum(nums)
#         if total % 2 == 1:
#             return False
#         target = total // 2
#         dp = [[False] * (target+1) for _ in range(n+1)]
#         for i in range(0, n+1):
#             dp[i][0] = True
#         for i in range(1, n+1):
#             for j in range(1, target + 1):
#                 if j >= nums[i-1]:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[n][target]


# solution = Solution()
# print(solution.canPartition([1, 2, 3, 5]))

# 【53】[零钱兑换2](https://leetcode-cn.com/problems/coin-change-2/)
# dp[i][j]：用 coins[..i] 凑出 j，共有 dp[i][j] 种方法
# base case: dp[0][j] = 0, dp[i][0] = 1
# 状态转移： dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n = len(coins)
#         dp = [[0] * (amount + 1) for _ in range(n + 1)]
#         for i in range(n+1):
#             dp[i][0] = 1
#         for i in range(1, n+1):
#             for j in range(1, amount + 1):
#                 if j >= coins[i-1]:
#                     dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[n][amount]


# solution = Solution()
# print(solution.change(3, [3]))


# 【322】[零钱兑换](https://leetcode-cn.com/problems/coin-change/)
# dp[i][j]：用 coins[..i] 凑出 j，最少用 dp[i][j] 个硬币
# base case: dp[0][j] = 2^31, dp[i][0] = 0
# 状态转移：dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
# 压缩，去掉 i 状态

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         intMax = amount + 1
#         dp = [intMax] * (amount + 1)
#         dp[0] = 0

#         for j in range(0, amount + 1):
#             for coin in coins:
#                 if j >= coin:
#                     dp[j] = min(dp[j], dp[j-coin] + 1)
#                 else:
#                     continue

#         return dp[amount] if dp[amount] != intMax else -1


# solution = Solution()
# print(solution.coinChange([1, 2, 5], 100))

# 【787】[K站中转内最便宜的航班](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)
# dp[k, dist]: 从起点出发，经过K站中转到达 dist 节点的最小步数
# base case: dp[0, src] = 0
# 转换： dp[dist, k] = min(dp[s1, k-1] + w1, dp[s2][k-1] + w2)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = [[float("inf")] * n for _ in range(k + 2)]
        f[0][src] = 0
        # IMPORTANT! 遍历方式
        for t in range(1, k + 2):
            for j, i, cost in flights:
                f[t][i] = min(f[t][i], f[t - 1][j] + cost)

        ans = min(f[t][dst] for t in range(1, k + 2))
        return -1 if ans == float("inf") else ans


solution = Solution()
print(solution.findCheapestPrice(
    4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
print(solution.findCheapestPrice(
    3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(solution.findCheapestPrice(3,
                                 [[0, 1, 2], [1, 2, 1], [2, 0, 10]],
                                 1,
                                 2,
                                 1))
