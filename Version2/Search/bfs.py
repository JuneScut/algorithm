# BFS, 没有可优化的子结构，不能用动态规划
from typing import List

# [79. 单词搜索](https://leetcode.cn/problems/word-search/?favorite=2cktkvj)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        self.found = False
        for i in range(m):
            for j in range(n):
                self.traverse(board, word, i, j, 0)
                if self.found:
                    return True
        return self.found

    # 从 board[i][j] 向四周扩散是否匹配 word[..p]
    def traverse(self, board: List[List[str]], word: str, i: int, j: int, p: int):
        if p == len(word):
            self.found = True
            return
        # 已经找到了一个答案，不用再搜索了
        if self.found:
            return
        m, n = len(board), len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if board[i][j] != word[p]:
            return
        # 加上负号，防止再次走到，类似 visited 的作用
        board[i][j] = '-' + board[i][j]
        self.traverse(board, word, i-1, j, p+1)
        self.traverse(board, word, i, j-1, p+1)
        self.traverse(board, word, i, j+1, p+1)
        self.traverse(board, word, i+1, j, p+1)
        # 撤销
        board[i][j] = board[i][j][1:]


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
# print(Solution().exist(board, word))
