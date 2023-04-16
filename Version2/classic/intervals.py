from typing import List

# [1288. 删除被覆盖区间](https://leetcode.cn/problems/remove-covered-intervals/)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 先排序，等于先确定了左边是否能包围
        # 按照起点升序相同排序，如果起点相同，按照终点降序排序
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        cross = 0
        for i in range(1, len(intervals)):
            cur = intervals[i]
            # 1. 覆盖
            if left <= cur[0] and right >= cur[1]:
                cross += 1
            # 2. 交叉
            elif left <= cur[0] and right <= cur[1]:
                right = cur[1]
            # 3. 不相关
            elif right <= cur[0]:
                left = cur[0]
                right = cur[1]
        return len(intervals)-cross

intervals = [[1,4],[1,2],[3,4]]
# print(Solution().removeCoveredIntervals(intervals))

# [56. 合并区间](https://leetcode.cn/problems/merge-intervals/?favorite=2cktkvj)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        left, right = intervals[0][0], intervals[0][1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            # 覆盖
            if left <= cur[0] and cur[1] <= right:
                continue
            # 交叉
            elif cur[0] <= right and right <= cur[1]:
                right = cur[1]
                res.pop()
                res.append([left, right])
            # 不相关
            elif right <= cur[0]:
                left = cur[0]
                right = cur[1]
                res.append(cur)
        return res

intervals = [[1,2],[1,4]]
print(Solution().merge(intervals))