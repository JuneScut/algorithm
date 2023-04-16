from typing import List

# [48. 旋转图像](https://leetcode.cn/problems/rotate-image/?favorite=2cktkvj)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 沿对角线翻转
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 翻转每一行
        for row in matrix:
            l, r = 0, n-1
            while l <= r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
        
matrix = [[1]]
# Solution().rotate(matrix)
# print(matrix)

# [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        upper, lower = 0, m-1
        left, right = 0, n-1
        res = []
        while len(res) < m*n:
            # 在上边，从左到右遍历
            if upper <= lower:
                for j in range(left, right+1):
                    res.append(matrix[upper][j])
                upper += 1
            # 在右边，从上到下遍历
            if left <= right:
                for i in range(upper, lower+1):
                    res.append(matrix[i][right])
                right -= 1
            # 在底部，从右到左遍历
            if upper <= lower:
                for j in range(right, left-1, -1):
                    res.append(matrix[lower][j])
                lower -= 1
            # 在左边，从下到上遍历
            if left <= right:
                for i in range(lower, upper-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res

matrix = [
    [1]]
# print(Solution().spiralOrder(matrix))

# [59. 螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/)
# 和上一道题一样，只不过改成赋值
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[-1]*n for _ in range(n)]
        upper, lower = 0, n-1
        left, right = 0, n-1
        cur = 1
        while cur <= n*n:
            # 在上边，从左到右赋值
            if upper <= lower:
                for j in range(left, right+1):
                    res[upper][j] = cur
                    cur += 1
                upper += 1
            # 在右边，从上到下赋值
            if left <= right:
                for i in range(upper, lower+1):
                    res[i][right] = cur
                    cur += 1
                right -= 1
            # 在底部，从右到左赋值
            if upper <= lower:
                for j in range(right, left-1, -1):
                    res[lower][j] = cur
                    cur += 1
                lower -= 1
            # 在左边，从下到上赋值
            if left <= right:
                for i in range(lower, upper-1, -1):
                    res[i][left] = cur
                    cur += 1
                left += 1
        return res

print(Solution().generateMatrix(4))


