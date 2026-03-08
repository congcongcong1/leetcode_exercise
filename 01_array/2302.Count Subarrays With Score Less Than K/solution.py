"""
LeetCode [2302]. [统计得分小于 K 的子数组数目]

难度: [Hard]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
一个数组的 分数 定义为数组之和 乘以 数组的长度。

比方说，[1, 2, 3, 4, 5] 的分数为 (1 + 2 + 3 + 4 + 5) * 5 = 75 。
给你一个正整数数组 nums 和一个整数 k ，请你返回 nums 中分数 严格小于 k 的 非空整数子数组数目。

子数组 是数组中的一个连续元素序列。
"""

from typing import List, Optional


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 分数计算的公式：sum(nums)*len(nums)
        # 思路：「越短越合法」型滑动窗口,看到子数组，那么必须用双指针滑动窗口的思想，枚举右指针，来超过题目分数条件，
        #一旦超过就移动左指针来满足条件
        
        left, ans = 0, 0
        current_sum = 0  # 维护窗口内的元素和
        
        for right, x in enumerate(nums):
            current_sum += x  # 右指针移入，累加和
            
            # 窗口长度为 (right - left + 1)
            # 如果分数 >= k，则不断收缩左边界
            while current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            # 此时以 right 为结尾的所有子数组都满足条件
            # 这些子数组的左起点可以是 left, left+1, ..., right
            # 数量正好是窗口的长度
            ans += (right - left + 1)
            
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
