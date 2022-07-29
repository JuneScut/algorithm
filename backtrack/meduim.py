# !/usr/bin/env python3
# coding=utf-8
from typing import List
from unittest import result

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
print(solution.findTargetSumWays([1, 1, 1, 1, 1], 3))
