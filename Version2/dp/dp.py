from typing import List

# [10. 正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/?favorite=2cktkvj)
# dp(s, i, p, j) 表示 s[i:] 是否能被 p[j:] 匹配


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        return self.dp(s, 0, p, 0)

    # 递归调用超出时间限制
    def dp(self, s: str, i: int, p: str, j: int) -> bool:
        m, n = len(s), len(p)
        # 边界考虑
        # 如 aa 和 a*b, aa 和 a*b*, aa 和 a*
        if j == n:
            return i == m
        if i == m:
            if (n-j) % 2 == 1:
                return False
            while j < (n-1):
                if p[j+1] != '*':
                    return False
                j += 2
            return True

        key = (i, j)
        if self.memo.get(key):
            return self.memo.get(key)

        res = False

        if s[i] == p[j] or p[j] == '.':
            # 也得看下一个是否是 '*'
            if j < (n - 1) and p[j+1] == '*':
                # 不匹配或者匹配多个
                res = self.dp(s, i, p, j+2) or self.dp(s, i+1, p, j)
            else:
                res = self.dp(s, i+1, p, j+1)
        else:
            # 不匹配，看下一个是否是 ’*‘, 是的话可以跳过，如 aa 和 b*aa
            if j < (n - 1) and p[j+1] == '*':
                res = self.dp(s, i, p, j+2)
            else:
                res = False

        self.memo[key] = res
        return res


s = "aaaaaaaaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*"
# print(Solution().isMatch(s, p))


#  dp(s, i, p, j+2)
#  dp(s, i+1, p, j)
#  dp(s, i+1, p, j+1)
# f[i][j] 表示 s 的前 i 个字符能否和 p 的前 j 个字符匹配上
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]


s = "aab"
p = "a*b"
# print(Solution().isMatch(s, p))

# [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/?favorite=2cktkvj)


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        # dp[i] 表示以 s[i-1] 结尾的字符所有的合法括号的数量
        # 用 +1 是方便为了下次去除 dp[leftIndex]
        dp = [0 for _ in range(n+1)]
        stack = []
        for (i, ch) in enumerate(s):
            if ch == '(':
                stack.append(i)
                dp[i+1] = 0
            else:
                if not stack:
                    dp[i+1] = 0
                else:
                    leftIndex = stack[len(stack)-1]  # 配对的左括号对应的索引
                    # i-leftIndex+1 此次配对的括号长度
                    dp[i+1] = dp[leftIndex] + i-leftIndex + 1
                    stack.pop()
        ret = 0
        for i in dp:
            ret = max(ret, i)
        return ret


s = ""
# print(Solution().longestValidParentheses(s))


# [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/?favorite=2cktkvj)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-99999 for _ in range(n+1)]
        for (idx, value) in enumerate(nums):
            dp[idx+1] = max(value, dp[idx]+value)
        ret = nums[0]
        for value in dp:
            ret = max(ret, value)
        return ret


nums = [5, 4, -1, 7, 8]
# print(Solution().maxSubArray(nums))

# [62. 不同路径](https://leetcode.cn/problems/unique-paths/?favorite=2cktkvj)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]：从起点走到 (i,j) 的路径数量
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[i][j]


m = 1
n = 1
# print(Solution().uniquePaths(m,n))

# [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/?favorite=2cktkvj)
# dp[i][j] 表示到达 (i,j) 时的最小路径和
# base case: i=0, j=0
# 状态转移 dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        # base case: 由于只能向右或者向下运动
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]


grid = [[1], [2], [3]]
# print(Solution().minPathSum(grid))

# [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/?favorite=2cktkvj)
# dp[i] 表示到达第 i 层有几种方法
# base case: dp[0] = 0, dp[1] = 1, dp[2] = 2
# 转移方程： dp[i] = dp[i-1] + dp[i-2]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


n = 3
# print(Solution().climbStairs(n))

# 70 ---> 状态压缩
# 1,2,3,5,8...


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(2, n):
            a, b = b, a+b
        return b


n = 2
# print(Solution().climbStairs(n))

# [72. 编辑距离](https://leetcode.cn/problems/edit-distance/?favorite=2cktkvj)
# dp[i][j]： 将  word1[...i] 转为 word2[...j] 的最小操作数
# base case:
# 状态转移：字符不相等时，
# dp[1][j] = min(
#       dp[i-1][j]+1,  # delete
#       dp[i][j-1]+1, # insert
#       dp[i-1][j-1]+1, # replace
# )


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(0, n+1):
            dp[0][j] = j
        for i in range(0, m+1):
            dp[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1,
                                   dp[i][j-1]+1,
                                   dp[i-1][j-1]+1)
        return dp[m][n]


word1 = "intention"
word2 = "i"
# print(Solution().minDistance(word1, word2))

# [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?favorite=2cktkvj)
# dp[i][0] 表示第 i 天未持有股票时的收益： dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
# dp[i][1] 表示第 i 天持有股票时的收益: dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]) = max(dp[i-1][1], -prices[i])
# 只限交易一次


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # base case, 第一天
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n-1][0]  # max(dp[n-1][0], dp[n-1][1]) 但未持有股票时收益必定更高

# 一维变量压缩


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit_0 = 0
        profit_1 = -prices[0]
        for i in range(1, n):
            profit_0 = max(profit_0, profit_1+prices[i])
            profit_1 = max(profit_1, -prices[i])
        return profit_0  # max(dp[n-1][0], dp[n-1][1]) 但未持有股票时收益必定更高

# print(Solution().maxProfit([7,1,5,3,6,4]))

# [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)
# 没有了购买次数的限制
# 和上一道题相比，只有 dp[i][1] 的条件需要改下


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit_0 = 0
        profit_1 = -prices[0]
        for i in range(1, n):
            profit_0 = max(profit_0, profit_1+prices[i])
            profit_1 = max(profit_1, profit_0-prices[i])
        return profit_0

# print(Solution().maxProfit([7,1,5,3,6,4]))


# [152. 乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/?favorite=2cktkvj)
# 🆚 [53. 最大子数组和]
# 由于乘积是可以负负得正的，所以还需要记录前一个位置的最小乘积和
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [nums[i] for i in range(n)]
        min_dp = [nums[i] for i in range(n)]
        for i in range(1, n):
            max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
        ret = -float('inf')
        for val in max_dp:
            ret = max(ret, val)
        return ret


nums = [-2, 0, 1]
# print(Solution().maxProduct(nums))

# [198. 打家劫舍](https://leetcode.cn/problems/house-robber/?favorite=2cktkvj)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [nums[i] for i in range(n)]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
