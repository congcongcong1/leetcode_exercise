"""
LeetCode 104. Maximum Depth of Binary Tree (二叉树的最大深度)

难度: Easy
链接: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
标签: 二叉树, DFS, BFS

题目描述:
    给定一个二叉树 root，返回其最大深度。
    最大深度是从根节点到最远叶子节点的最长路径上的节点数。
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        """
        解法一: 递归 (DFS)

        思路:
            树的最大深度 = 1 + max(左子树深度, 右子树深度)

        时间复杂度: O(n) — 每个节点访问一次
        空间复杂度: O(h) — h 为树高，最坏 O(n)
        """
        if not root:
            return 0
        left_depth = self.maxDepth_recursive(root.left)
        right_depth = self.maxDepth_recursive(root.right)
        return 1 + max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        解法二: 层序遍历 (BFS)

        思路:
            用队列层序遍历，每遍历一层，深度加 1。

        时间复杂度: O(n)
        空间复杂度: O(n) — 最宽层的节点数
        """
        if not root:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1: [3,9,20,null,null,15,7] → 深度 3
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.maxDepth_recursive(root) == 3, "测试用例 1 失败"
    assert sol.maxDepth(root) == 3, "测试用例 1 BFS 失败"

    # 测试用例 2: [1,null,2] → 深度 2
    root = TreeNode(1, None, TreeNode(2))
    assert sol.maxDepth(root) == 2, "测试用例 2 失败"

    # 测试用例 3: 空树
    assert sol.maxDepth(None) == 0, "测试用例 3 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
