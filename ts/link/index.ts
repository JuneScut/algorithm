import PriorityQueue from "../priorityQueue";

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// 🌼 [21 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)
function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let head = new ListNode(-1);
  let cur = head;
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      cur.next = list1;
      list1 = list1.next;
    } else {
      cur.next = list2;
      list2 = list2.next;
    }
    cur = cur.next;
    cur.next = null;
  }
  if (list1) {
    cur.next = list1;
  }
  if (list2) {
    cur.next = list2;
  }
  return head.next;
}
let l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
let l2 = new ListNode(1, new ListNode(3, new ListNode(4)));
let p = mergeTwoLists(l1, l2);
// while (p) {
//   console.log(p.val);
//   p = p.next;
// }

// 🌼 [86 分隔链表](https://leetcode.cn/problems/partition-list/)
function partition(head: ListNode | null, x: number): ListNode | null {
  const dummy1 = new ListNode(-1),
    dummy2 = new ListNode(-1);
  let p1 = dummy1,
    p2 = dummy2;
  let p = head;
  while (p) {
    if (p.val < x) {
      p1.next = p;
      p1 = p1.next;
    } else {
      p2.next = p;
      p2 = p2.next;
    }
    p = p.next;
  }
  p2.next = null;
  p1.next = dummy2.next;
  return dummy1.next;
}
p = new ListNode(
  1,
  new ListNode(
    4,
    new ListNode(3, new ListNode(2, new ListNode(5, new ListNode(2))))
  )
);
// let result = partition(p, 3);
// while (result) {
//   console.log(result.val);
//   result = result.next;
// }

function enqueue(arr: ListNode[], item: ListNode) {
  arr.push(item);
  arr.sort((a, b) => a.val - b.val);
}
// [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  if (lists.length == 0) return null;
  const dummy = new ListNode(-1);
  let p = dummy;
  let pq: ListNode[] = [];
  for (let item of lists) {
    if (item) enqueue(pq, item);
  }
  while (pq.length > 0) {
    const cur = pq.shift() || null;
    p.next = cur;
    if (cur?.next) {
      enqueue(pq, cur.next);
    }
    if (p.next) p = p.next;
  }
  return dummy.next;
}
let p1 = new ListNode(1, new ListNode(4, new ListNode(5)));
let p2 = new ListNode(1, new ListNode(3, new ListNode(4)));
let p3 = new ListNode(2, new ListNode(6));
// let result = mergeKLists([p1, p2, p3]);
// while (result) {
//   console.log(result.val);
//   result = result.next;
// }

// [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/)
function detectCycle(head: ListNode | null): ListNode | null {
  let fast = head,
    slow = head;
  while (slow && fast && fast.next) {
    fast = fast.next ? fast.next.next : null;
    slow = slow.next ? slow.next : null;
    if (fast == slow) {
      break;
    }
  }
  if (fast == null || fast.next == null) {
    // fast 遇到空指针说明没有环
    return null;
  }
  // 有环，一个在起点，一个在相遇点同时出发直至相遇
  slow = head;
  while (slow != fast) {
    slow = slow?.next || null;
    fast = fast?.next || null;
  }
  return slow;
}

// [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list/)
function reverseList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;
  let last = reverseList(head.next);
  head.next.next = head;
  head.next = null;
  return last;
}

function reverseList2(head: ListNode | null): ListNode | null {
  let cur = head;
  let prev: ListNode | null = null;
  while (cur) {
    let next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }
  return prev;
}
p1 = new ListNode(1, new ListNode(4, new ListNode(5)));
reverseList2(p1);
