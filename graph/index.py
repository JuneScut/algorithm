
import heapq
from typing import List

# 【797】 [所有可能路径](https://leetcode.cn/problems/all-paths-from-source-to-target/)


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        path = []
        self.travel(graph, 0, path)
        return self.res

    def travel(self, graph: List[List[int]], s: int, path: List[int]):
        path.append(s)
        if s == len(graph)-1:
            self.res.append(path[:])
        for v in graph[s]:
            self.travel(graph, v, path)
        path.pop()


solution = Solution()
# print(solution.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]))

# 【1514】[概率最大的路径](https://leetcode.cn/problems/path-with-maximum-probability/)
# Dijkstra 算法


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # 构造 graph：List[tuple]
        graph = [[] for _ in range(n)]
        for i, edge in enumerate(edges):
            fromPoint, toPoint = edge[0], edge[1]
            weight = succProb[i]
            # 无向图也就是双向图
            graph[fromPoint].append((toPoint, weight))
            graph[toPoint].append((fromPoint, weight))
        return self.dijkstra(start, end, graph)

    def dijkstra(self, start: int, end: int, graph: List[tuple]):
        n = len(graph)
        distTo = [0.0] * n  # 记录从 start 到每个节点的最大概率
        distTo[start] = 1

        q = [(-1.0, start)]
        while q:
            curState = heapq.heappop(q)  # 优先队列，贪心优化
            curDistFromState, curNode = curState
            curVal = -curDistFromState

            # 不需要记录所有的点了，提高时间
            if curNode == end:
                return curVal

            # 减枝
            if curVal < distTo[curNode]:
                continue

            for (nextNodeId, weight) in graph[curNode]:
                distToNextNode = distTo[curNode] * weight
                if distToNextNode > distTo[nextNodeId]:
                    distTo[nextNodeId] = distToNextNode
                    heapq.heappush(q, (-distToNextNode, nextNodeId))

        return distTo[end]


solution = Solution()
# print(solution.maxProbability(
#     3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2))


# 【743】[](https://leetcode.cn/problems/network-delay-time/)
