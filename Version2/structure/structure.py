# [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/?favorite=2cktkvj)
# OrderedDict, 相当于 LinkeHashMap in java
import collections


class LRUCache:
    def __init__(self, capacity: int):
        self.capcity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capcity:
                # 链表头部就是最久未使用的 key
                # FIFO if last = False
                self.cache.popitem(last=False)
            self.cache[key] = value


# lRUCache = LRUCache(2)
# print(lRUCache.put(2, 1))
# print(lRUCache.put(1, 1))
# print(lRUCache.put(2, 3))
# print(lRUCache.put(4, 1))
# print(lRUCache.get(1))
# print(lRUCache.get(2))


# [155. 最小栈](https://leetcode.cn/problems/min-stack/?favorite=2cktkvj)
# 用额外的栈空间维护最小值
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
