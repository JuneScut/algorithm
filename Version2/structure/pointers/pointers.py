from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
# DFS 算法，backtrack 
def traverse(root: TreeNode):
    if not root:
        return
    
    print(f"进入节点：{root.left.val if root.left else None}")
    traverse(root.left)
    print(f"离开节点：{root.left.val if root.left else None}")
    print(f"进入节点：{root.right.val if root.right else None}")
    traverse(root.right)
    print(f"离开节点：{root.right.val if root.right else None}")

traverse(root)

print("==========")

# DFS 算法，图遍历
def traverse2(root: TreeNode):
    if not root:
        return
    print(f"进入节点：{root.val if root else None}")
    traverse2(root.left)
    traverse2(root.right)
    print(f"离开节点：{root.val if root else None}")

traverse2(root)
    




