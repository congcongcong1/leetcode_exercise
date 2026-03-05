"""
LeetCode 704. Binary Search (二分查找)

难度: Easy
链接: https://leetcode.cn/problems/binary-search/
标签: 二分查找

题目描述:
    给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，
    写一个函数搜索 target，如果存在返回下标，否则返回 -1。
"""

from typing import List


class Solution:
    def search_closed(self, nums: List[int], target: int) -> int:
        """
        解法一: 左闭右闭 [left, right]

        思路:
            在 [left, right] 区间内查找，while left <= right

        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:  # [left, right] 区间有效条件
            mid = left + (right - left) // 2  # 防止溢出

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # target 在右半部分 [mid+1, right]
            else:
                right = mid - 1  # target 在左半部分 [left, mid-1]

        return -1

    def search(self, nums: List[int], target: int) -> int:
        """
        解法二: 左闭右开 [left, right)

        思路:
            在 [left, right) 区间内查找，while left < right

        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums)

        while left < right:  # [left, right) 区间有效条件
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # target 在 [mid+1, right)
            else:
                right = mid      # target 在 [left, mid)

        return -1


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1: 目标值在数组中
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4, "测试用例 1 失败"

    # 测试用例 2: 目标值不在数组中
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1, "测试用例 2 失败"

    # 测试用例 3: 单元素数组
    assert sol.search([5], 5) == 0, "测试用例 3 失败"

    # 测试用例 4: 单元素，未找到
    assert sol.search([5], -5) == -1, "测试用例 4 失败"

    # 两种写法交叉验证
    assert sol.search_closed([-1, 0, 3, 5, 9, 12], 9) == 4, "左闭右闭 验证失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
