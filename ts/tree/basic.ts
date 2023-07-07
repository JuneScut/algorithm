/**
 * Definition for a binary tree node.
 */
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// 🐠 前序遍历
function preOrder(root: TreeNode): number[] {
  const res: number[] = [];
  if (!root) {
    return res;
  }
  res.push(root.val);
  if (root.left) {
    res.push(...preOrder(root.left));
  }
  if (root.right) {
    res.push(...preOrder(root.right));
  }
  return res;
}
let tree = new TreeNode(
  1,
  new TreeNode(2, new TreeNode(4), new TreeNode(5)),
  new TreeNode(3, new TreeNode(6), new TreeNode(7))
);

let res = preOrder(tree); // [1, 2, 4, 5, 3, 6, 7]
// console.log(JSON.stringify(res));

// 🐠 打印每一个节点所在的层数
function printLevel(root: TreeNode | null, level: number = 0): void {
  if (!root) {
    return;
  }
  console.log(root.val, level);
  printLevel(root.left, level + 1);
  printLevel(root.right, level + 1);
}

// 🐠 打印出每个节点的左右子树各有多少节点？
function countTreeNodes(root: TreeNode | null): number {
  if (!root) {
    return 0;
  }
  const leftCount = countTreeNodes(root.left);
  const rightCount = countTreeNodes(root.right);
  console.log(
    `node value: ${root.val}, left: ${leftCount}, right: ${rightCount}`
  );
  return leftCount + rightCount + 1;
}
// countTreeNodes(tree);

// 🐠 dfs 思路，针对每个节点
function dfs(root: TreeNode | null): void {
  if (!root) return;
  console.log(`enter node: ${root.val}`);
  // 多叉树改循环
  dfs(root.left);
  dfs(root.right);
  console.log(`leave node: ${root.val}`);
}

// 🐠 backtrack 思路，针对每个树枝
function backtrack(root: TreeNode | null): void {
  if (!root) return;
  // 多叉树改循环
  console.log(
    `Enter: node ${root.val} to node ${root.left ? root.left.val : null}`
  );
  backtrack(root.left);
  console.log(
    `Leave node ${root.val} to node ${root.left ? root.left.val : null}`
  );

  console.log(
    `Enter: node ${root.val} to node ${root.right ? root.right.val : null}`
  );
  backtrack(root.right);
  console.log(
    `Leave node ${root.val} to node ${root.right ? root.right.val : null}`
  );
}

// 🐠 层序遍历思路
function levelTraverse(root: TreeNode | null) {
  if (!root) return;
  const q: TreeNode[] = [];
  q.push(root);
  while (q.length > 0) {
    const size = q.length;
    for (let i = 0; i < size; i++) {
      const item = q.shift();
      if (item) {
        console.log(`Node: ${item.val}`);
        if (item.left) q.push(item.left);
        if (item.right) q.push(item.right);
      }
    }
  }
}
levelTraverse(tree);

// 🪷 [104 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)
function maxDepth(root: TreeNode | null): number {
  if (!root) return 0;
  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
tree = new TreeNode(
  3,
  new TreeNode(9),
  new TreeNode(20, new TreeNode(15), new TreeNode(7))
);
// console.log(maxDepth(tree));

// 🪷 [543 二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)
function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;
  function maxDepth(root: TreeNode | null): number {
    if (!root) return 0;
    const leftDepth = maxDepth(root.left);
    const rightDepth = maxDepth(root.right);
    const diameter = leftDepth + rightDepth;
    maxDiameter = Math.max(diameter, maxDiameter);
    return Math.max(leftDepth, rightDepth) + 1;
  }
  maxDepth(root);
  return maxDiameter;
}

tree = new TreeNode(
  1,
  new TreeNode(2, new TreeNode(4), new TreeNode(5)),
  new TreeNode(3)
);
let result = diameterOfBinaryTree(tree);
// console.log(result);

// [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/)
function invertTree(root: TreeNode | null): TreeNode | null {
  if (!root) return null;
  const temp = root.left;
  root.left = root.right;
  root.right = temp;
  invertTree(root.left);
  invertTree(root.right);
  return root;
}

// [116. 填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)
class Node2 {
  val: number;
  left: Node2 | null;
  right: Node2 | null;
  next: Node2 | null;
  constructor(val?: number, left?: Node2, right?: Node2, next?: Node2) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
    this.next = next === undefined ? null : next;
  }
}
function connect(root: Node2 | null): Node2 | null {
  function traverse(left: Node2 | null, right: Node2 | null): void {
    if (!left || !right) return;
    left.next = right.next;
    traverse(left.left, left.right);
    traverse(left.right, right.left);
    traverse(right.left, right.right);
  }
  if (!root) return null;
  traverse(root.left, root.right);
  return root;
}

// [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)
function flatten(root: TreeNode | null): void {
  if (!root) return;
  flatten(root.left);
  flatten(root.right);
  const left = root.left;
  const right = root.right;
  root.right = left;
  root.left = null;
  let p = root;
  while (p.right) {
    p = p.right;
  }
  p.right = right;
}

// [654. 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)
function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
  if (nums.length == 0) {
    return null;
  }
  let maxVal = Number.MIN_SAFE_INTEGER;
  let maxValIndex = -1;
  for (let idx = 0; idx < nums.length; idx++) {
    const val = nums[idx];
    if (val > maxVal) {
      maxVal = val;
      maxValIndex = idx;
    }
  }
  const root = new TreeNode(maxVal);
  root.left = constructMaximumBinaryTree(nums.slice(0, maxValIndex));
  root.right = constructMaximumBinaryTree(
    nums.slice(maxValIndex + 1, nums.length)
  );
  return root;
}
constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]);

// [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
  function build(
    preorder: number[],
    preStart: number,
    preEnd: number,
    inorder: number[],
    inStart: number,
    inEnd: number
  ): TreeNode | null {
    if (preStart > preEnd || inStart > inEnd) return null;
    const rootVal = preorder[preStart];
    const root = new TreeNode(rootVal);
    const rootIdx = inorder.indexOf(rootVal);
    const leftChildLength = rootIdx - inStart;
    root.left = build(
      preorder,
      preStart + 1,
      preStart + leftChildLength,
      inorder,
      inStart,
      rootIdx
    );
    root.right = build(
      preorder,
      preStart + leftChildLength + 1,
      preEnd,
      inorder,
      rootIdx + 1,
      inEnd
    );
    return root;
  }
  return build(
    preorder,
    0,
    preorder.length - 1,
    inorder,
    0,
    inorder.length - 1
  );
}

// [106. 从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
function buildTree2(inorder: number[], postorder: number[]): TreeNode | null {
  function build(
    inorder: number[],
    instart: number,
    inend: number,
    postorder: number[],
    poststart: number,
    postend: number
  ): TreeNode | null {
    if (instart > inend || poststart > postend) return null;
    const rootVal = postorder[postend];
    const root = new TreeNode(rootVal);
    const index = inorder.indexOf(rootVal);
    const leftSize = index - instart;

    root.left = build(
      inorder,
      instart,
      index - 1,
      postorder,
      poststart,
      poststart + leftSize - 1
    );

    root.right = build(
      inorder,
      index + 1,
      inend,
      postorder,
      poststart + leftSize,
      postend - 1
    );
    return root;
  }
  return build(
    inorder,
    0,
    inorder.length - 1,
    postorder,
    0,
    postorder.length - 1
  );
}
