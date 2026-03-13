"""
LeetCode [209]. [长度最小的子数组]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/
标签: [数组, 双指针, 排序]

题目描述:
定一个含有 n 个正整数的数组和一个正整数 target 
找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] 
并返回其长度。如果不存在符合条件的子数组，返回 0 
"""

from typing import List, Optional


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 思路：利用双指针，然后遍历右指针
        # 时间复杂度：O(n)
        # 空间复杂度: O(1)
        n = len(nums)
        ans = n + 1
        left = 0
        s = 0
        for right,x in enumerate(nums): # x = nums[right]
            s += x
            # while的单调性，从符合要求变成不符合要求
            while s >=target:
                ans = min(ans, right-left+1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0



# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1
    assert sol.minSubArrayLen(7,[2,3,1,2,4,3]) == 2, "测试用例 1 失败"

    # 测试用例 2
    assert sol.solve([]) == None, "测试用例 2 失败"

    # 边界case
    # assert sol.solve([]) == None, "边界case 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
