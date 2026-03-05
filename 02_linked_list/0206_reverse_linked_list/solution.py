"""
LeetCode 206. Reverse Linked List (反转链表)

难度: Easy
链接: https://leetcode.cn/problems/reverse-linked-list/
标签: 链表

题目描述:
    给你单链表的头节点 head，请你反转链表，并返回反转后的链表。
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法一: 迭代法（双指针）

        思路:
            用 prev 和 curr 两个指针，逐个翻转 next 指针方向。

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next  # 先保存下一个节点
            curr.next = prev       # 翻转指针方向
            prev = curr            # prev 前进
            curr = next_temp       # curr 前进
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        解法二: 递归法

        思路:
            递归到链表末尾，然后回溯时翻转指针。
            关键：head.next.next = head 实现翻转。

        时间复杂度: O(n)
        空间复杂度: O(n) — 递归栈
        """
        # 终止条件：空链表或只有一个节点
        if not head or not head.next:
            return head

        # 递归反转后面的部分
        new_head = self.reverseList(head.next)

        # 翻转当前节点的指针
        head.next.next = head
        head.next = None

        return new_head


# ==================== 辅助函数 ====================

def list_to_linked(arr):
    """将数组转换为链表"""
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linked_to_list(head):
    """将链表转换为数组"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1
    head = list_to_linked([1, 2, 3, 4, 5])
    result = sol.reverseList_iterative(head)
    assert linked_to_list(result) == [5, 4, 3, 2, 1], "测试用例 1 失败"

    # 测试用例 2
    head = list_to_linked([1, 2])
    result = sol.reverseList(head)
    assert linked_to_list(result) == [2, 1], "测试用例 2 失败"

    # 测试用例 3: 空链表
    result = sol.reverseList(None)
    assert linked_to_list(result) == [], "测试用例 3 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
