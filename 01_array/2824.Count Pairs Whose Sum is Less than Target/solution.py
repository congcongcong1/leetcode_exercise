"""
LeetCode [2824]. [Count Pairs Whose Sum is Less than Target]

难度: [Easy]
链接: https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
标签: [数组, 双指针, 排序]

题目描述:
    给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，
    请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目
"""

from typing import List, Optional


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        解法一:  双指针

        思路:
        先对数组进行排序，然后用双指针法，左右指针加起来如果小于target，那么就可以返回之间的所有数,同时左指针往右移动1；
        如果加起来大于target，此时区间内的所有数和右指针加起来都会比target大，因此无需考虑num[right]
        所以就把右指针往左移，直到小于target，重复以上过程

        时间复杂度: O(nlogn)
        空间复杂度: O(1)
        """
        nums.sort() #先从小到大排序 排序复杂度为O(nlogn)
        cnt = 0
        left, right = 0,len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                cnt += right - left
                left += 1
            else:
                right -= 1
        return cnt

    def solve_v2(self, nums: List[int]) -> int:
        """
        解法二: 左右指针法

        思路:
        由于数组是有序的，所以可以使用左右指针法，当左右指针加起来的值小于target，那么需要移动左指针一格，如果大于target，那么需要移动右指针一格，直到找到target。

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left , right = 0 , len(nums)-1
        while left < right:
             if nums[left] + nums[right] == target:
                return [left+1,right+1]
             elif nums[left] + nums[right] < target:
                left += 1
             else:
                right -= 1
        return []
       


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
