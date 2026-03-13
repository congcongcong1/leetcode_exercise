"""
LeetCode [713]. [和小于 K 的子数组]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/
标签: [数组, 双指针, 排序]

题目描述:
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
"""

from typing import List, Optional


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        #思路： 注意到是正整数，用双指针维护一个滑动窗口，枚举右指针，让这个滑动窗口内的乘积都小于k后计算子数组
        # l r 之间 那么子数组有[l,r] [l+1,r],[l+2,r]……[r,r] 一共有l-r+1个子数组
        # 时间复杂度o(n) 
        # 空间复杂度o(1)
        n = len(nums)
        if k <= 1: return 0
        left, product, ans =0, 1, 0
        for right, x in enumerate(nums):
            product *= x
            while product >= k :
                product /= nums[left]
                left += 1
            ans += right -left + 1
        return ans



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
