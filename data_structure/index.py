import queue


# 【232】 [用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/)
class MyQueue:

    def __init__(self):
        self.stack1 = []  # 队尾
        self.stack2 = []  # 队头

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


class MyStack:

    def __init__(self):
        self.q = queue([])

    def push(self, x: int) -> None:
        self.topEle = x

    def pop(self) -> int:
        pass

    def top(self) -> int:
        pass

    def empty(self) -> bool:
        pass


# 【设计循环队列】[622](https://leetcode.cn/problems/design-circular-queue/)
class MyCircularQueue:

    def __init__(self, k: int):
        self.queque = [None] * (k+1)
        self.front = 0
        self.rear = 0
        self.capicity = k+1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            # 表示已满
            return False
        self.queque[self.rear] = value
        self.rear = (self.rear + 1) % self.capicity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queque[self.front] == None
        self.front = (self.front + 1) % self.capicity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[self.rear-1]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear+1) % self.capicity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# circularQueue = MyCircularQueue(3)
# param_1 = circularQueue.enQueue(1)
# param_2 = circularQueue.enQueue(2)
# param_3 = circularQueue.enQueue(3)
# param_4 = circularQueue.enQueue(4)

# param_5 = circularQueue.Rear()
# param_6 = circularQueue.isFull()
# param_7 = circularQueue.deQueue()
# param_8 = circularQueue.enQueue(4)
# param_9 = circularQueue.Rear()


# 【641】 [设计循环双端队列](https://leetcode.cn/problems/design-circular-deque/)
class MyCircularDeque:

    def __init__(self, k: int):
        self.queque = [None] * (k+1)
        self.capicity = k + 1
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front-1) % self.capicity
        self.queque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queque[self.rear] = value
        self.rear = (self.rear+1) % self.capicity
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queque[self.front] = None
        self.front = (self.front+1) % self.capicity
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear-1) % self.capicity
        self.queque[self.rear] = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queque[(self.rear-1) % self.capicity]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capicity == self.front


# Your MyCircularQueue object will be instantiated and called as such:
circularQueue = MyCircularDeque(8)
param_3 = circularQueue.insertFront(5)
param_4 = circularQueue.getFront()
param_6 = circularQueue.isEmpty()
param_6 = circularQueue.deleteFront()


param_5 = circularQueue.getRear()
param_6 = circularQueue.isFull()
param_7 = circularQueue.deleteLast()
param_8 = circularQueue.insertFront(4)
param_9 = circularQueue.getFront()
