"""
LeetCode 1. Two Sum (两数之和)

难度: Easy
链接: https://leetcode.cn/problems/two-sum/
标签: 数组, 哈希表

题目描述:
    给定一个整数数组 nums 和一个整数目标值 target，
    找出数组中和为目标值 target 的两个整数，返回它们的下标。
    假设每种输入只会对应一个答案，且不能重复使用同一元素。
"""

from typing import List


class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        """
        解法一: 暴力枚举

        思路:
            两层循环，逐一检查所有数对是否和为 target。

        时间复杂度: O(n²)
        空间复杂度: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        解法二: 哈希表  枚举右，寻找左

        思路:
            遍历数组，对于每个元素 x，检查 target - x 是否在哈希表中。
            如果在，直接返回两个下标；如果不在，将 x 及其下标存入哈希表。

        时间复杂度: O(n) — 只需一次遍历
        空间复杂度: O(n) — 哈希表存储
        """
        hash_map = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
        return []


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
