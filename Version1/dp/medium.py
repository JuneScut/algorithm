# !/usr/bin/env python3
# coding=utf-8
import collections
from math import log2
from mimetypes import init
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) + 1
        n = len(text2) + 1
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                # 因为是从 1 开始，所以需要 -1
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]


solution = Solution()
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
# print(solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


# 【416】[分隔等和子集](https://leetcode-cn.com/problems/partition-equal-subset-sum/)
# 背包问题，有 n 个物品 nums, 背包重量恰好为 sums(nums) / 2
# 状态：i 个物品，背包重量 j
# dp[i][j] 定义：前 i 个物品，是否能装满重量为 j, base case: dp[0][...] = 0, dp[...][0] = 1
# 转移：dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
# 一维压缩, TODO:
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False] * (target+1) for _ in range(n+1)]
        for i in range(0, n+1):
            dp[i][0] = True
        for i in range(1, n+1):
            for j in range(1, target + 1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]

    def canPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [False] * (total+1)

        # base case
        dp[0] = True
        for i in range(0, n):
            for j in range(target, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]

        return dp[target]


solution = Solution()
# print(solution.canPartition2([1, 5, 11, 5]))

# 【53】[零钱兑换2](https://leetcode-cn.com/problems/coin-change-2/)
# dp[i][j]：用 coins[..i] 凑出 j，共有 dp[i][j] 种方法
# base case: dp[0][j] = 0, dp[i][0] = 1
# 状态转移： dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount + 1):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount]


# solution = Solution()
# print(solution.change(3, [3]))


# 【322】[零钱兑换](https://leetcode-cn.com/problems/coin-change/)
# 定义状态为 amount
# 确定 base case 为 amount=0 时硬币为 0
# base case: dp[0][j] = 2^31, dp[i][0] = 0
# dp[j]：用 coins[..i] 凑出 j，最少用 dp[j] 个硬币
# 状态转移：dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]]+1)
# 压缩，去掉 i 状态

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)  # amount+1 作为一个标记符,就相当于初始化为正无穷

        # base case
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[amount] == amount+1 else dp[amount]


solution = Solution()
print(solution.coinChange([1], 0))

# 【787】[K站中转内最便宜的航班](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)
# dp[k, dist]: 从起点出发，经过K站中转到达 dist 节点的最小步数
# base case: dp[0, src] = 0
# 转换： dp[dist, k] = min(dp[s1, k-1] + w1, dp[s2][k-1] + w2)


# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         f = [[float("inf")] * n for _ in range(k + 2)]
#         f[0][src] = 0
#         # IMPORTANT! 遍历方式
#         for t in range(1, k + 2):
#             for j, i, cost in flights:
#                 f[t][i] = min(f[t][i], f[t - 1][j] + cost)

#         ans = min(f[t][dst] for t in range(1, k + 2))
#         return -1 if ans == float("inf") else ans


# solution = Solution()
# print(solution.findCheapestPrice(
#     4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))
# print(solution.findCheapestPrice(
#     3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
# print(solution.findCheapestPrice(3,
#                                  [[0, 1, 2], [1, 2, 1], [2, 0, 10]],
#                                  1,
#                                  2,
#                                  1))


# 【516】[最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         # 状态： i, j 表示字符串区间的起始和终点
#         n = len(s)
#         dp = [[0] * n for _ in range(n)]
#         # base case
#         for i in range(n):
#             dp[i][i] = 1
#         # 状态转移，从末尾到头反过来遍历，因为下一个状态是 dp[i-1][j] 和 dp[i][j-1]
#         for i in range(n-1, -1, -1):
#             for j in range(i+1, n, 1):
#                 if s[i] == s[j]:
#                     dp[i][j] = dp[i+1][j-1] + 2
#                 else:
#                     dp[i][j] = max(dp[i+1][j], dp[i][j-1])

#         return dp[0][n-1]


# solution = Solution()
# print(solution.longestPalindromeSubseq("bbbab"))


# 【931】 [下降路径最小和](https://leetcode.cn/problems/minimum-falling-path-sum/)
# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         res = 99999
#         n = len(matrix)
#         # 初始化备忘录
#         self.memo = [[666666] * n for _ in range(n)]
#         # 结果在最后一行中选择
#         for j in range(n):
#             res = min(res, self.dp(matrix, n-1, j))
#         return res

#     def dp(self, matrix: List[List[int]], i: int, j: int) -> int:
#         # base case
#         if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
#             return 99999
#         if i == 0:
#             return matrix[0][j]
#         # 查找备忘录：
#         if self.memo[i][j] != 666666:
#             return self.memo[i][j]
#         # 状态转移：
#         self.memo[i][j] = matrix[i][j] + min(
#             self.dp(matrix, i-1, j-1),
#             self.dp(matrix, i-1, j),
#             self.dp(matrix, i-1, j+1),
#         )
#         return self.memo[i][j]


# solution = Solution()
# print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))

# 【1048】 [最长字符串链](https://leetcode.cn/problems/longest-string-chain/)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def check(pre, post):
            cnt = 0
            m = len(post)
            x = 0
            for k in range(m):
                if post[k] == pre[x]:
                    x += 1
                else:
                    cnt += 1
                if cnt >= 2:
                    return False
                if x == len(pre):
                    break
            return True
        words.sort(key=lambda x: len(x))
        dct = collections.defaultdict(list)
        n = len(words)
        dp = [1]*n
        for i in range(n):
            for j in dct[len(words[i])-1]:
                if check(words[j], words[i]) and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
            dct[len(words[i])].append(i)
        return max(dp)


solution = Solution()
# print(solution.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]))


# 【674】 [最长连续递增序列](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        start = 0

        for i in range(n):
            if i > 0 and nums[i] <= nums[i-1]:
                start = i
            else:
                dp[i] = i - start + 1
                res = max(res, dp[i])
        return res


# solution = Solution()
# print(solution.findLengthOfLCIS([2, 2, 2, 2, 2]))

# 【198】 [打家劫舍](https://leetcode.cn/problems/house-robber/)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] 表示在[0..i] 能偷到的最大值
        # 状态：偷与不偷
        # 转移方程：max(dp[i-2]+nums[i], dp[i-1])
        n = len(nums)
        # base case
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # 状态转移
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n, 1):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]


# solution = Solution()
# print(solution.rob([2, 7, 9, 3, 1]))

# 【279】 [完全平方数](https://leetcode.cn/problems/perfect-squares/)
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] 表示数字 i 的最小完全平方数
        # base case: dp[1] = 1
        # 状态：是否使用某个平方数
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i  # 最差情况，都由1组成
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]


# solution = Solution()
# print(solution.numSquares(1))

# 【213】[打家劫舍II](https://leetcode.cn/problems/house-robber-ii/)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start, end):
            # 计算区间[start, end]的最优解, 压缩了 dp 状态
            first = nums[start]
            second = max(first, nums[start+1])
            for i in range(start+2, end+1):
                first, second = second, max(first+nums[i], second)
            return second

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(1, n-1), robRange(0, n-2))


# solution = Solution()
# print(solution.rob([2, 3, 2]))

# 【337】[打家劫舍III](https://leetcode.cn/problems/house-robber-iii/)
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.memo.get(root, -1) != -1:
            return self.memo.get(root)
        robIt = root.val + (self.rob(root.left.left) + self.rob(root.left.right) if root.left else 0) + \
            (self.rob(root.right.left) +
             self.rob(root.right.right) if root.right else 0)
        unRobIt = self.rob(root.left) + self.rob(root.right)
        res = max(robIt, unRobIt)
        self.memo[root] = res
        return res

# 【不同路径】[62](https://leetcode.cn/problems/unique-paths/)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 从起点走到 （i，j）的不同路径数
        # 状态：从哪边过来
        dp = [[0] * n for _ in range(m)]
        # base case
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]


solution = Solution()
# print(solution.uniquePaths(7, 3))

# 【不同路径II】[63](https://leetcode.cn/problems/unique-paths-ii/)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while i < m and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1
        while j < n and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


solution = Solution()
# print(solution.uniquePathsWithObstacles([[1, 0]]))

# 【121】[买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)
# 这里注意只能购买一次


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n-1][0]

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n-1][0]

    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        if n >= 1:
            dp[0][0] = 0
            dp[0][1] = -prices[0]
        if n >= 2:
            dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
            dp[1][1] = max(dp[0][1],  -prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1],  dp[i-2][0]-prices[i])

        return dp[n-1][0]

    def maxProfit5(self, prices: List[int]) -> int:
        n = len(prices)
        max_k = 2
        dp = [[[0] * 2 for _ in range(max_k+1)] for _ in range(n)]

        for i in range(0, n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    # base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[0]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][max_k][0]


solution = Solution()
# print(solution.maxProfit5([3, 3, 5, 0, 0, 3, 1, 4]))
