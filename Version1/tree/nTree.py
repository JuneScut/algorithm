# !/usr/bin/env python3
# coding=utf-8

from functools import reduce
from itertools import chain
import operator
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        result = []
        if root.children != None:
            for node in root.children:
                result.extend(self.postorder(node))
            result.append(root.val)
        else:
            result.append(root.val)
        return result


solution = Solution()
print(solution.postorder(Node(1, [
      Node(3, [
          Node(5, None),
          Node(6, None)]),
      Node(2, None), Node(4, None)
      ])))
