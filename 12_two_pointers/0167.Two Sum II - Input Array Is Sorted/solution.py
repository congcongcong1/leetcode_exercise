"""
LeetCode [167]. [两数之和 II - 输入有序数组]

难度: [Medium]
链接: https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
标签: [数组, 双指针, 排序]

题目描述:
    给你一个整数数组 numbers ，该数组已按<em>非递减顺序排列</em> ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

    以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2 。

    你可以假设每个输入<strong>只对应唯一的答案</strong> ，而且你<strong>不可以</strong>重复使用相同的元素。

    你所设计的解决方案必须只使用常量级的额外空间 即O(1)。
"""

from typing import List, Optional


class Solution:
    def solve(self, nums: List[int]) -> int:
        """
        解法一:  暴力枚举

        思路:
        这里的第一想法是直接遍历数组，对于每个元素，遍历数组中剩余的元素，看是否存在两个元素的和等于目标值。

        时间复杂度: O(n^2) 不符合要求
        空间复杂度: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range (i+1,n):
                if nums[i]+nums[j] == target:
                    return[i+1,j+1] #因为下标是从1开始的
        return []

    def solve_v2(self, nums: List[int]) -> int:
        """
        解法二: 左右指针法

        思路:
        由于数组是有序的，所以可以使用左右指针法，当左右指针加起来的值小于target，那么需要移动左指针一格，如果大于target，那么需要移动右指针一格，直到找到target。

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        pass


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1
    assert sol.solve([]) == None, "测试用例 1 失败"

    # 测试用例 2
    assert sol.solve([]) == None, "测试用例 2 失败"

    # 边界case
    # assert sol.solve([]) == None, "边界case 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
