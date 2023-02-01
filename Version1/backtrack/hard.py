# !/usr/bin/env python3
# coding=utf-8


from typing import List

from pyparsing import col

# 回溯算法，关注：
# 1. 路径：也就是已经做出的选择
# 2. 选择列表：也就是当前可以做的选择
# 3. 结束条件：也就是到达决策树的底层，无法再做选择的条件
# [N皇后](https://leetcode-cn.com/problems/n-queens/)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        def isValid(board, row, column):
            # print(board, row, column)
            i, j = 0, 0
            # 检查当前列
            while i < row:
                if board[i][column] == 'Q':
                    # print("                    列", i)
                    return False
                i += 1
            i, j = row - 1, column + 1
            # 检查右上方
            while i >= 0 and j < len(board):
                if board[i][j] == 'Q':
                    # print("                    右上方", i, j)
                    return False
                i -= 1
                j += 1
            i, j = row - 1, column - 1
            # 检查左上方
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    # print("                    左上方", i, j)
                    return False
                i -= 1
                j -= 1
            # print(True)
            return True

        def backtrack(board, row):
            # 结束条件
            if row == n:
                res.append(["".join(irow) for irow in board])
                return
            # 列举
            for i in range(n):
                # 做选择
                if not isValid(board, row, i):
                    continue
                board[row][i] = 'Q'
                backtrack(board, row + 1)
                # 撤销
                board[row][i] = '.'

        backtrack(board, 0)
        return res


solution = Solution()
print(solution.solveNQueens(8))
