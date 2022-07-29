# !/usr/local/bin/env python3
# coding=utf-8
from typing import List

# 【506】[相对名次](https://leetcode-cn.com/problems/relative-ranks/)


class Solution:
    desc = ("Gold Medal", "Silver Medal", "Bronze Medal")

    def findRelativeRanks2(self, score: List[int]) -> List[str]:
        ans = [""] * len(score)
        arr = sorted(enumerate(score), key=lambda x: -x[1])
        for i, (idx, _) in enumerate(arr):
            ans[idx] = self.desc[i] if i < 3 else str(i + 1)
        return ans

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if not score:
            return []
        min, max = score[0], score[0]
        # 找到区间
        for item in score:
            if item > max:
                max = item
            if item < min:
                min = item
        baseList = [-1 for x in range(0, max - min + 1)]
        index = 0
        # 创建区间下标数组
        while index < len(score):
            bais = score[index] - min
            baseList[bais] = index
            index += 1
        result = ['' for x in range(0, len(score))]
        rank = 1
        while max >= min:
            index = max - min
            if (baseList[index] >= 0):
                if rank == 1:
                    result[baseList[index]] = "Gold Medal"
                elif rank == 2:
                    result[baseList[index]] = "Silver Medal"
                elif rank == 3:
                    result[baseList[index]] = "Bronze Medal"
                else:
                    result[baseList[index]] = f"{rank}"
                rank += 1
            max -= 1
        return result


solution = Solution()
print(solution.findRelativeRanks2([5, 4, 3, 2, 1]))
