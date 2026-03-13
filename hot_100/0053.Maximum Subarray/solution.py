"""
LeetCode [53]. [最大子数组]

难度: [Hard]
链接: https://leetcode.cn/problems/maximum-subarray/   
标签: [数组, 动态规划，贪心]

题目描述:
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""

from typing import List, Optional


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 解法：前缀和+贪心，即不能让过去的失败影响到现在
        # 求连续子数组的最大和，连续子数组求和可以想到维护一个前缀和数组S[0]=0,S[n+1]= S[n]+nums[n]
        # 易出错点：子数组的和必须是右边的前缀和减去左边的前缀和。
        # 至于求最大值，思路是用当前的前缀和减去之前的最小前缀和就是目前最大值，不断更新
        # 时间复杂度:O(n)
        # 空间复杂度:O(1)
        min_s = 0 # 最小前缀和
        cur_s = 0 # 目前为止的前缀和
        ans = -inf
        for i,x in enumerate(nums):
            cur_s += x
            ans = max(ans,cur_s - min_s)
            min_s = min(cur_s,min_s)
        return  ans




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
