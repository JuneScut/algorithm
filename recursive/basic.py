# coding=utf-8
# 1239. 串联字符串的最大长度
# 回溯算法 二叉树  每个节点都有两种情况

# class Solution(object):
#     def maxLength(self, arr):
#         """
#         :type arr: List[str]
#         :rtype: int
#         """
#         filteredArr = []
#         for str in arr:
#             if len(set(str)) == len(str):
#                 filteredArr.append(str)
#         arr = filteredArr[:]

#         def dfs(index, tmp):
#             if(index >= len(arr)):
#                 return len(tmp)

#             flag = set(tmp) & set(arr[index])
#             if(not flag):
#                 return max(dfs(index+1, tmp+arr[index]), dfs(index+1, tmp))
#             else:
#                 return dfs(index+1, tmp)

#         return dfs(0, "")

# solution = Solution()
# print(solution.maxLength(["cha","r","act","ers"]))

# 79 单词搜索
# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
#         wordLenIdx = len(word) -1
#         rLen = len(board)
#         if rLen == 0:
#             return False
#         cLen = len(board[0])

#         marked = [[False for _ in range(cLen)] for _ in range(rLen)]

#         def dfs(index, i, j):
#             if index == wordLenIdx:
#                 return board[i][j] == word[index]

#             flag = word[index] == board[i][j]
#             if flag:
#                 marked[i][j] = True
#                 for direction in directions:
#                     newX = i + direction[0]
#                     newY = j + direction[1]
#                     if 0 <= newX and newX < rLen and 0 <= newY and newY < cLen and not marked[newX][newY] and dfs(index+1, newX, newY):
#                         return True
#                 marked[i][j] = False
#             return False


#         for idx in range(rLen):
#             for jdx in range(cLen):
#                 if dfs(0, idx, jdx):
#                     return True
#         return False

# solution = Solution()
# print(solution.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCB"
# ))

# 200 海岛数量
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """

#         def inArea(grid, r, c):
#             return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]) if len(grid) > 0 else False

#         def dfs(grid, r, c):
#             if inArea(grid, r, c) == False:
#                 return
#             if grid[r][c] != '1':
#                 return
#             grid[r][c] = '2'
#             dfs(grid, r+1, c)
#             dfs(grid, r, c+1)
#             dfs(grid, r-1, c)
#             dfs(grid, r, c-1)

#         count = 0
#         for r in range(0, len(grid)):
#             for c in range(0, len(grid[0])):
#                 if grid[r][c] == '1':
#                     dfs(grid, r, c)
#                     count += 1

#         return count


# solution = Solution()
# print(solution.numIslands([
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]))


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if (len(board) == 0):
            return

        def inArea(board, r, c):
            return 0 <= r and r < len(board) and 0 <= c and c < len(board[0])

        def dfs(board, r, c):
            if inArea(board, r, c) == False:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = 'A'
            dfs(board, r+1, c)
            dfs(board, r-1, c)
            dfs(board, r, c+1)
            dfs(board, r, c-1)

        # 遍历边界
        rLen = len(board)
        cLen = len(board[0])
        for i in range(0, rLen):
            dfs(board, i, 0)
            dfs(board, i, cLen - 1)
        for j in range(0, cLen):
            dfs(board, 0, j)
            dfs(board, rLen-1, j)

        for r in range(0, rLen):
            for c in range(0, cLen):
                if board[r][c] == 'A':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                print(board[r][c], end=" ")
            print("")


solution = Solution()
grid = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', "O", 'O'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
]
solution.solve(grid)
