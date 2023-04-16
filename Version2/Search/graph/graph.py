# 图遍历框架
# 📢 由于可能存在环，所以需要增加一个 visited 数组判断是否之前经过
# 🍀 图更加关注的是节点是否访问过，所以撤销操作在循环外边，把所有的子节点都访问过了才撤销
# 🍀 回溯算法更加关注的是路径，所以撤销操作在循环里边
# // 记录被遍历过的节点
# boolean[] visited;
# // 记录从起点到当前节点的路径
# boolean[] onPath;

# /* 图遍历框架 DFS */
# void traverse(Graph graph, int s) {
#     if (visited[s]) return;
#     // 经过节点 s，标记为已遍历
#     visited[s] = true;
#     // 做选择：标记节点 s 在路径上
#     onPath[s] = true;
#     for (int neighbor : graph.neighbors(s)) {
#         traverse(graph, neighbor);
#     }
#     // 撤销选择：节点 s 离开路径
#     onPath[s] = false;
# }

import heapq
from typing import List


# [797. 所有可能的路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.traverse(graph, [], 0)
        return self.res

    # cur 当前访问节点
    def traverse(self, graph: List[List[int]], onPath: List[int], cur: int):
        onPath.append(cur)
        n = len(graph)  # 最后一个节点=n-1
        # 判断是否可以收集
        if cur == n-1:
            self.res.append(onPath[:])
        for child in graph[cur]:
            self.traverse(graph, onPath, child)
        # 撤销选择
        onPath.pop()


graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# print(Solution().allPathsSourceTarget(graph))

#  [207. 课程表](https://leetcode.cn/problems/course-schedule/?favorite=2cktkvj)
# 遍历图 -> 转换为邻接表
# 检查是否存在环, 增加一个 onPath 路径，判断是否有经过目前遍历的点了
# bfs


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.buildGraph(prerequisites)
        self.hasCycle = False
        visited = [False for _ in range(numCourses)]
        onPath = []
        for i in range(numCourses):
            self.traverse(onPath, visited, i)
        return not self.hasCycle

    def buildGraph(self, prerequisites: List[List[int]]):
        for (cur, pre) in prerequisites:
            self.graph[pre].append(cur)  # 增加依赖关系，放入到邻接表中

    def traverse(self, onPath: List[int], visited: List[int], cur: int):
        if cur in onPath:
            self.hasCycle = True
        if self.hasCycle or visited[cur]:
            return
        for node in self.graph[cur]:
            onPath.append(cur)
            visited[cur] = True
            self.traverse(onPath, visited, node)
            onPath.pop()


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# print(Solution().canFinish(numCourses, prerequisites))


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.buildGraph(prerequisites)
        self.hasCycle = False
        self.postorder = []  # 记录后续遍历的结果
        self.visited = [False for _ in range(numCourses)]
        self.onPath = [False for _ in range(numCourses)]
        for i in range(numCourses):
            self.traverse(i)
        if self.hasCycle:
            return []
        self.postorder.reverse()
        return self.postorder

    def buildGraph(self, prerequisites: List[List[int]]):
        for (cur, pre) in prerequisites:
            self.graph[pre].append(cur)  # 增加依赖关系，放入到邻接表中

    def traverse(self, cur: int):
        if self.onPath[cur]:
            self.hasCycle = True
        if self.hasCycle or self.visited[cur]:
            return
        self.onPath[cur] = True
        self.visited[cur] = True
        for node in self.graph[cur]:
            self.traverse(node)
        self.onPath[cur] = False
        self.postorder.append(cur)


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# print(Solution().findOrder(numCourses, prerequisites))

# [743 网络延迟时间](https://leetcode.cn/problems/network-delay-time/)


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.graph = [[] for _ in range(n+1)]
        self.buildGraph(times)
        distTo = self.dijkstra(k, n)
        ret = max(distTo[1:])
        return ret if ret != float('inf') else -1

    # 邻接表，存储节点和权重

    def buildGraph(self, times: List[List[int]]):
        for [start, end, weight] in times:
            self.graph[start].append([end, weight])

    def dijkstra(self, start: int, n: int):
        # 从起点到该点的距离
        distTo = [float('inf') for _ in range(n+1)]
        distTo[start] = 0
        priorityList = []
        heapq.heappush(priorityList, [0, start])  # [距离，节点]，距离放在前面，方便排序
        while priorityList:
            [curDist, curNodeId] = heapq.heappop(priorityList)
            if curDist > distTo[curNodeId]:
                continue  # 还没走到下一个节点就已经距离太大
            # 将 cur 的相邻节点装入队列
            for child in self.graph[curNodeId]:
                [endPoint, weight] = child
                if distTo[endPoint] > curDist + weight:
                    # 可以更新
                    distTo[endPoint] = curDist + weight
                    heapq.heappush(priorityList, [distTo[endPoint], endPoint])
        return distTo


times = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
n = 3
k = 1
# print(Solution().networkDelayTime(times, n, k))

# [1631. 最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/)


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.m = len(heights)
        self.n = len(heights[0])
        # 定义：从 (0, 0) 到 (i, j) 的最小体力消耗是 effortTo[i][j]
        effortTo = [[float('inf') for _ in range(self.n)]
                    for _ in range(self.m)]
        # base case
        effortTo[0][0] = 0
        priorityList = []
        heapq.heappush(priorityList, (0, 0, 0))  # effort, x, y
        while priorityList:
            cur_effort, x, y = heapq.heappop(priorityList)
            # 到达终点
            if x == self.m - 1 and y == self.n - 1:
                return cur_effort
            # 这条路的 effort 过大，继续走没有意义
            if cur_effort > effortTo[x][y]:
                continue
            # 将 cur 的相邻节点装入队列
            for next_x, next_y in self.adj(x, y):
                next_effort = max(cur_effort, abs(
                    heights[x][y] - heights[next_x][next_y]))
                if next_effort < effortTo[next_x][next_y]:
                    effortTo[next_x][next_y] = next_effort
                    heapq.heappush(priorityList, (next_effort, next_x, next_y))
        return -1

    def adj(self, x: int, y: int):
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for (add_x, add_y) in dirs:
            new_x = x + add_x
            new_y = y + add_y
            if new_x < 0 or new_x >= self.m or new_y < 0 or new_y >= self.n:
                continue
            neighbors.append((new_x, new_y))
        return neighbors


heights = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [
    1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
# print(Solution().minimumEffortPath(heights))

# [1514. 概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        m = len(edges)
        self.graph = [[] for _ in range(n+1)]  # 邻接表
        for i in range(m):
            from_node, to_node = edges[i]
            self.graph[from_node].append([to_node, succProb[i]])
            self.graph[to_node].append([from_node, succProb[i]])
        priorityList = []
        # probTo[i] 的值就是节点 start 到达节点 i 的最大概率
        probTo = [-1 for _ in range(n+1)]
        probTo[start] = 1
        # [概率，节点]，概率放在前面，方便排序，要把最大的概率放在前边
        heapq.heappush(priorityList, [1*-1, start])
        while priorityList:
            curProb, cur = heapq.heappop(priorityList)
            curProb = curProb * -1
            # 已经到达终点
            if cur == end:
                return curProb
            # 将 cur 的相邻节点装入队列
            for (next_node, edge_pro) in self.graph[cur]:
                nextProb = curProb * edge_pro
                if nextProb > probTo[next_node]:
                    # 可以更新
                    probTo[next_node] = nextProb
                    heapq.heappush(priorityList, [nextProb*-1, next_node])
        return 0.0


n = 3
edges = [[0, 1]]
succProb = [0.5]
start = 0
end = 2
print(Solution().maxProbability(n, edges, succProb, start, end))
