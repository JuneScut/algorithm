# 爬楼梯
# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         """
#         :type cost: List[int]
#         :rtype: int
#         """
#         costLen = len(cost)
#         if costLen <= 1:
#             return 0
#         memo = [ 0 for _ in range(costLen + 1)]
#         memo[0] = 0
#         memo[1] = 0
#         for index in range(2, len(memo)):
#             memo[index] = min(memo[index-1] + cost[index-1], memo[index-2] + cost[index-2])
#         return memo[costLen]

# solution = Solution()
# print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


# 392 判断子序列
# 很难想到这道也可以用DP
# class Solution(object):
#     def isSubsequence(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         sLen = len(s)
#         tLen = len(t)
#         if sLen > tLen:
#             return False
#         i = 0
#         j = 0
#         while i < sLen and j < tLen:
#             if s[i] == t[j]:
#                 i = i + 1
#                 j = j + 1
#             else:
#                 j = j + 1
#         return True if ( i == sLen and j <= tLen ) else False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         n, m = len(s), len(t)
#         f = [[0] * 26 for _ in range(m)]
#         f.append([m] * 26)

#         for i in range(m - 1, -1, -1):
#             for j in range(26):
#                 f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        
#         add = 0
#         for i in range(n):
#             if f[add][ord(s[i]) - ord('a')] == m:
#                 return False
#             add = f[add][ord(s[i]) - ord('a')] + 1
        
#         return True

# solution = Solution()
# print(solution.isSubsequence("abc", "ahbgdc"))