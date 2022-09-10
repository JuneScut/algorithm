# !/usr/bin/env python3
# coding=utf-8
from ntpath import join
from typing import List
from unittest import result
from xmlrpc.client import Boolean

from numpy import arange

# 【46】[全排列](https://leetcode.cn/problems/permutations/)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        if len(track) == len(nums):
            self.res.append(track[:])
            return
        for i in range(0, len(nums)):
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False


solution = Solution()
# print(solution.permute([1, 2, 3]))

# 【53】 [N皇后](https://leetcode.cn/problems/n-queens/)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [['.'] * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board: List[str], row: int):
        # 达到临界条件
        if row == len(board):
            self.res.append(list(map(lambda item: ''.join(item), board)))
            return
        # 还是一个全排列问题，所以这里需要从0开始
        for col in range(0, len(board)):
            if not self.isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row+1)
            board[row][col] = '.'

    def isValid(self, board, row, col) -> bool:
        # 检查 board[row, col] 是否能放下皇后
        # 检查同一列
        for r in range(0, row):
            if board[r][col] == 'Q':
                return False
        # 检查右斜线：
        r, c = row-1, col+1
        while r >= 0 and c < len(board):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
        # 检查左斜线：
        r, c = row-1, col-1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        return True


solution = Solution()
# print(solution.solveNQueens(1))


# 【494】[目标和](https://leetcode-cn.com/problems/target-sum/)
# python 回溯超时，改为动态规划


class Solution:
    result = 0

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def backtrack(res, idx):
            # 结束条件
            if idx == n:
                if res == target:
                    self.result += 1
                return
            # 做选择, +
            res += nums[idx]
            backtrack(res, idx+1)
            # 恢复, 做选择, -
            res -= nums[idx] * 2
            backtrack(res, idx + 1)

        backtrack(0, 0)

        return self.result

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums, n = sum(nums), len(nums)
    # 设fu为nums中被选为前面加-号的数字之和，则有正数为sum-fu，又有(sum-fu)-fu=target，即fu=(sum-target)/2，并根据nums[i]>=0，可知sum-target应为非负偶数
        fu = (sum_nums-target)//2
        if (sum_nums-target) < 0 or (sum_nums-target) & 1:
            return 0
    # dp[i][j]：nums前i位中取部分元素使其和为j的方法总数，则目标为dp[n][fu]
        dp = [[0] * (fu + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            nums_i = nums[i - 1]
            for j in range(fu + 1):
                # nums[i]太大了，不能选
                if j < nums_i:
                    dp[i][j] = dp[i-1][j]
                # num[i]可选可不选
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums_i]
        return dp[n][fu]


solution = Solution()
# print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))

# 【78】[子集](https://leetcode.cn/problems/subsets/)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.trace = []
        self.backtrack2(nums, 0)
        return self.res

    def backtrack(self, nums, start: int):
        if start == len(nums):
            self.res.append(self.trace[:])
            return
        self.trace.append(nums[start])
        self.backtrack(nums, start+1)
        self.trace.pop()
        self.backtrack(nums, start+1)

    def backtrack2(self, nums, start: int):
        self.res.append(self.trace[:])

        for i in range(start, len(nums)):
            self.trace.append(nums[i])
            self.backtrack2(nums, i+1)
            self.trace.pop()


solution = Solution()
# print(solution.subsets([1, 2, 3]))

# 【77】 [组合](https://leetcode.cn/problems/combinations/)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.track = []
        self.backtrack(n, 1, k)
        return self.res

    def backtrack(self, n: int, start: int, k: int):
        if len(self.track) == k:
            self.res.append(self.track[:])

        for i in range(start, n+1):
            self.track.append(i)
            self.backtrack(n, i+1, k)
            self.track.pop()


solution = Solution()
# print(solution.combine(4, 2))

# 【90】[子集II](https://leetcode.cn/problems/subsets-ii/)
# 数组有可重复元素，但不可重复选


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.track = []
        nums.sort()
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums: List[int], start: int):
        self.res.append(self.track[:])
        for i in range(start, len(nums)):
            # 减枝, 值相同的相邻枝条，只遍历第一条
            if i > start and nums[i] == nums[i-1]:
                continue
            self.track.append(nums[i])
            self.backtrack(nums, i+1)
            self.track.pop()


solution = Solution()
# print(solution.subsetsWithDup([2, 1, 2]))
#
# 【40】 [组合总和II](https://leetcode.cn/problems/combination-sum-ii/)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.track = []
        self.trackSum = 0
        self.target = target
        candidates.sort()
        self.backtrack(candidates, 0)
        return self.res

    def backtrack(self, candidates: List[int], start: int):
        if self.trackSum == self.target:
            self.res.append(self.track[:])
        if self.trackSum > self.target:
            return
        for i in range(start, len(candidates)):
            # 减枝逻辑
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.track.append(candidates[i])
            self.trackSum += candidates[i]
            self.backtrack(candidates, i+1)
            self.trackSum -= candidates[i]
            self.track.pop()


solution = Solution()
# print(solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

# 【47】[全排列II](https://leetcode.cn/problems/permutations-ii/)


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.track = []
        used = [False] * len(nums)
        nums.sort()
        self.backback(nums, used)
        return self.res

    def backback(self, nums: List[int], used: List[bool]):
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return
        for i in range(0, len(nums)):
            if used[i]:
                continue
            # 这里的减枝逻辑
            if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                continue
            used[i] = True
            self.track.append(nums[i])
            self.backback(nums, used)
            self.track.pop()
            used[i] = False


solution = Solution()
# print(solution.permuteUnique([3, 3, 0, 3]))

# 【39】[组合总数](https://leetcode.cn/problems/combination-sum/)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.track = []
        self.trackSum = 0
        self.backtrack(candidates, 0, target)
        return self.res

    def backtrack(self, nums: List[int], start: int, target: int):
        if self.trackSum == target:
            self.res.append(self.track[:])
            return
        if self.trackSum > target:
            return
        for i in range(start, len(nums)):
            self.track.append(nums[i])
            self.trackSum += nums[i]
            self.backtrack(nums, i, target)
            self.trackSum -= nums[i]
            self.track.pop()


solution = Solution()
print(solution.combinationSum([2, 3, 5], 8))
