# !/usr/bin/env python3
# coding=utf-8
import collections
from math import log2


# 10 正则匹配
# 状态 dp[i,j] 表示s的前i个字符和p的前j个字符能否匹配上
# 状态转移方程：
# s[i] = p[j]  dp[i][j] = dp[i-1][j-1]

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m, n = len(s), len(p)

#         def matches(i: int, j: int) -> bool:
#             if i == 0:
#                 return False
#             if p[j - 1] == '.':
#                 return True
#             return s[i - 1] == p[j - 1]

#         f = [[False] * (n + 1) for _ in range(m + 1)]
#         f[0][0] = True
#         for i in range(m + 1):
#             for j in range(1, n + 1):
#                 if p[j - 1] == '*':
#                     f[i][j] |= f[i][j - 2]
#                     if matches(i, j - 1):
#                         f[i][j] |= f[i - 1][j]
#                 else:
#                     if matches(i, j):
#                         f[i][j] |= f[i - 1][j - 1]
#         return f[m][n]


# solution = Solution()
# print(solution.isMatch("aab", "a**"))

# 【174】[地下城游戏](https://leetcode-cn.com/problems/dungeon-game/)
# dp[i][j] 从 dungeon[i][j] 走到右下角的最小步数
# base case: dp[m-1][n-1] = dungeon[m-1][n-1] > 0 ? 1 : -dungeon[m-1][n-1] + 1
# 转移： dp[i][j], res = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], dp[i][j] = res <= 0 ? 1 : res
# class Solution:
#     def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
#         BIG = 10**9
#         dp = [[BIG] * (n+1) for _ in range(m+1)]
#         dp[m][n - 1] = dp[m - 1][n] = 1

#         for i in range(m - 1, -1, -1):
#             for j in range(n - 1, -1, -1):
#                 res = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
#                 dp[i][j] = 1 if res <= 0 else res

#         return dp[0][0]


# solution = Solution()
# print(solution.calculateMinimumHP([
#     [-2, -3, 3],
#     [-5, -10, 1],
#     [10, 30, -5]
# ]))

# 【514】[自由之路](https://leetcode-cn.com/problems/freedom-trail/)
# dp(ring, i, key, j): 表示当前位置在 ring[i], 划到 key[j...] 的最小操作数
# dp(ring, 0, key, 0) 为所求
# base case: dp(ring, i, key, m) = 0
# 转移： dp(ring, i, key, j) = min(顺时针操作，逆时针操作数) + dp(ring, i, key, j + 1) + 1
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         findCharIndex = {}
#         for index, char in enumerate(ring):
#             item = findCharIndex.get(char)
#             if item:
#                 item.append(index)
#             else:
#                 findCharIndex[char] = [index]
#         m, n = len(ring), len(key)
#         memo = [[0] * n for _ in range(m)]

#         def dp(ring: str, i: int, key: str, j: int):
#             if j == len(key):
#                 return 0
#             if memo[i][j] != 0:
#                 return memo[i][j]
#             res = 10 ** 9
#             for k in findCharIndex[key[j]]:
#                 delta = abs(k-i)
#                 delta = min(delta, m-delta)
#                 subProblem = dp(ring, k, key, j+1)
#                 res = min(res, delta + 1 + subProblem)
#             memo[i][j] = res
#             return res

#         return dp(ring, 0, key, 0)
#     # dp 数组版本, dp[i][j] 从 i 出发，到 ring[j] 和 key[j] 相同的位置，最少需要多少步

#     def findRotateSteps2(self, ring: str, key: str) -> int:
#         n = len(ring)
#         m = len(key)
#         dp = [[float('inf')]*n for _ in range(m)]
#         # lookup 统计key中的各字符出现的位置
#         lookup = collections.defaultdict(list)
#         for i in range(n):
#             lookup[ring[i]].append(i)
#         # dp 初始化，
#         for i in lookup[key[0]]:
#             dp[0][i] = min(i, n-i)+1

#         for i in range(1, m):
#             for j in lookup[key[i]]:  # key[i]字符出现的位置
#                 for k in lookup[key[i-1]]:  # key[i-1]字符出现的位置
#                     # t计算的是上一个字符原本位置是k的被移动到了12:00,
#                     # 那么当前字符位置是j的距离k的最短距离是多少
#                     if j > k:
#                         t = min(j-k, n-(j-k))
#                     else:
#                         t = min(k-j, n-(k-j))
#                     dp[i][j] = min(dp[i][j], dp[i-1][k]+1+t)
#         return min(dp[-1])


# solution = Solution()
# print(solution.findRotateSteps("godding", "godding"))
# print(solution.findRotateSteps2("godding", "gd"))

# 【887】[鸡蛋掉落](https://leetcode-cn.com/problems/super-egg-drop/)
# dp(k, n) 给定 k 枚🥚 检测从 n 层楼试验的最小操作数
# base case: dp(k, 0) = 0, dp(k, 1) = n
# 选择，从 N 层楼中选择每一层扔🥚
# 转移： dp(k,n) = min(dp(k,n), max(dp(k-1, n-1), dp(k, i)) + 1)
class Solution:
    # dp
    def superEggDrop(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k, n) -> int:
            if n == 0:
                return 0
            if k == 1:
                return n
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('INF')
            for i in range(1, n + 1):
                res = min(res, max(dp(k-1, i-1), dp(k, n-i)) + 1)
            memo[(k, n)] = res
            return res

        return dp(k, n)
    # dp + 数学优化

    def superEggDrop2(self, k: int, n: int) -> int:
        memo = dict()

        def dp(k, n) -> int:
            if n == 0:
                return 0
            if k == 1:
                return n
            if (k, n) in memo:
                return memo[(k, n)]
            lo, hi = 1, n
            # keep a gap of 2 x values to manually check later
            while lo + 1 < hi:
                x = (lo + hi) // 2
                t1 = dp(k - 1, x - 1)
                t2 = dp(k, n - x)

                if t1 < t2:
                    lo = x
                elif t1 > t2:
                    hi = x
                else:
                    lo = hi = x
            res = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                          for x in (lo, hi))
            memo[(k, n)] = res
            return res

        return dp(k, n)


solution = Solution()
print(solution.superEggDrop(3, 14))
print(solution.superEggDrop2(3, 14))
