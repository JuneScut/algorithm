// 自定义比较函数
interface A {
  val: number;
}
function compare(a: A, b: A) {
  return a.val - b.val;
}

// 优先队列类
class PriorityQueue {
  private queue: A[];
  constructor() {
    this.queue = [];
  }

  enqueue(element: A) {
    this.queue.push(element);
    this.queue.sort(compare); // 每次插入元素后，重新排序队列
  }

  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    return this.queue.shift();
  }

  isEmpty() {
    return this.queue.length === 0;
  }

  size() {
    return this.queue.length;
  }
}

// 使用示例
const pq = new PriorityQueue();
pq.enqueue({ val: 5 });
pq.enqueue({ val: 3 });
pq.enqueue({ val: 7 });

while (!pq.isEmpty()) {
  const element = pq.dequeue();
  console.log(element);
}

export default PriorityQueue;
