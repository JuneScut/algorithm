import sys

# https://www.nowcoder.com/practice/d3d8e23870584782b3dd48f26cb39c8f?tpId=37&tqId=21253&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fdifficulty%3D4%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=4&judgeStatus=undefined&tags=&title=

# [s1, s2] = input().split(' ')
# s = s1 + s2
# odds = []
# evens = []
# for i in range(len(s)):
#     if i % 2 == 0:
#         evens.append(s[i])
#     else:
#         odds.append(s[i])
# odds.sort()
# evens.sort()
# newS = []
# i, j, k = 0, 0, 0
# while i < len(s):
#     if i % 2 == 0:
#         newS.append(evens[j])
#         j += 1
#     else:
#         newS.append(odds[k])
#         k += 1
#     i += 1
# s = ''.join(newS)
# newS = []
# for ch in s:
#     if ord('0') <= ord(ch) <= ord('9') or ord('a') <= ord(ch) <= ord('f') or ord('A') <= ord(ch) <= ord('F'):
#         binArr = list(str(bin(int(f'0x{ch}', 16))[2:]).zfill(4))
#         binArr.reverse()
#         binVal = ''.join(binArr)
#         newCh = str(hex(int(f'0b{binVal}', 2)))[2:].upper()
#         newS.append(newCh)
#     else:
#         newS.append(ch)
# print(''.join(newS))

###################################

[m, n] = list(map(int, input().split(' ')))
i = 0
grid = []
while i < m:
    row = list(map(int, input().split(' ')))
    grid.append(row)
    i += 1

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
visited = [[False] * n for _ in range(m)]
path = [[0, 0]]
visited[0][0] = True
res = []


def dfs(x, y, visited):
    if x == m-1 and y == n-1 and grid[x][y] == 0:
        global res
        res = path[:][:]
        return

    for (addX, addY) in dirs:
        row, col = x+addX, y+addY
        if row < 0 or row >= m or col < 0 or col >= n:
            continue
        if visited[row][col]:
            continue
        if grid[row][col] == 1:
            continue
        if 0 <= row < m and 0 <= col < n and grid[row][col] == 0:
            visited[row][col] = True
            path.append([row, col])
            dfs(row, col, visited)
            path.pop()
            visited[row][col] = False


dfs(0, 0, visited)
for path in res:
    print(f'({path[0]},{path[1]})')
