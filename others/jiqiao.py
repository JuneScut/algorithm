from typing import List

# 【303】 [区域和检索](https://leetcode.cn/problems/range-sum-query-immutable/)
# 技巧题，由于 sumRange 会重复多次调用


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.preSum = [0] * (n+1)
        for i in range(1, n+1, 1):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1] - self.preSum[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
# print(numArray.sumRange(2, 5))

# 【304】 [二维区域和检索](https://leetcode.cn/problems/range-sum-query-2d-immutable/)


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.preSum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1, 1):
            for j in range(1, n+1, 1):
                self.preSum[i][j] = self.preSum[i][j-1] + \
                    self.preSum[i-1][j] - \
                    self.preSum[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]


numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [
                      1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
# print(numMatrix.sumRegion(1, 2, 2, 4))

li = []

# try:
#     while True:
#         line = input()
#         if line == '':
#             break
#         # lines = line.split()
#         # 转为整型list
#         # lines = list(map(int, lines))
#         # 将lines列表作为元素存入li列表
#         li.append(line)
# except:
#     pass

# print(li)

# params = []
# try:
#     while True:
#         line = input()
#         if line == '':
#             break
#         params.append(line)
# except:
#     pass

# arr = params[0]
# memo = {}
# for val in arr:
#     uVal = str.upper(val)
#     memo[uVal] = memo.get(uVal, 0) + 1

# print(memo.get(str.upper(params[1]), 0))

# n = int(input())
# count = 0
# arr = []
# while count < n:
#     arr.append(int(input()))
#     count += 1
# arr.sort()
# print(arr)


# line = input()
# directions =['A', 'D', 'W', 'S']

# def isLegalCord(str1):
#     if not str1:
#         return [False, 0]
#     if line(str1) < 2:
#         return [False, 0]
#     direction = str1[0]
#     if directions.index(direction) >= 0:
#         return [str1[1:].isdigit(), int(str1[1:])]
#     return [False, 0]

# x = 0
# y = 0
# arr = line.split(';')
# for step in arr:
#     result = isLegalCord(step)
#     if result[0]:
#         direction = step[0]
#         val = result[1]
#         if direction == 'A':
#             x += val
#         elif direction == 'D':
#             x -= val
#         elif direction == 'W':
#             y += val
#         elif direction == 'S':
#             y -= val

# print(f'{x},{y}')

def f(n, x):

    # n为待转换的十进制数，x为机制，取值为2-16
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n//x  # 商
        y = n % x  # 余数
        b = b+[y]
        if s == 0:
            break
        n = s
    b.reverse()
    for i in b:
        print(a[i], end='')


f(44, 8)
