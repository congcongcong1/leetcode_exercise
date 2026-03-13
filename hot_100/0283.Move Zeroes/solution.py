"""
LeetCode 283. 移动0

难度: Medium
链接: https://leetcode.cn/problems/two-sum/
标签: - 数组 双指针

题目描述:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 核心思路：题目要求保持非零元素的相对顺序，所有有一种快慢双指针的思想，慢指针用于指示位置，将所有非零元素按相对顺序排列，而快指针则遍历整个数组，寻找非零元素与慢指针进行替换
        # 时间复杂度:O(n) 
        # 空间复杂度:O(1)
        slow = 0 # 慢指针，用于指示非零元素的位置
        for fast, num in enumerate(nums):
            if num != 0 :
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1: 基础情况
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1], "测试用例 1 失败"

    # 测试用例 2: 答案在数组中间
    assert sol.twoSum([3, 2, 4], 6) == [1, 2], "测试用例 2 失败"

    # 测试用例 3: 相同元素
    assert sol.twoSum([3, 3], 6) == [0, 1], "测试用例 3 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
