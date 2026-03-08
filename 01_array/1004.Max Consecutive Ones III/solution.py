"""
LeetCode [1004]. [最大连续1的个数 III]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
给定一个二进制数组 nums 和一个整数 k，假设最多可以翻转 k 个 0，
则返回执行操作后 数组中连续 1 的最大个数。
"""

from typing import List, Optional


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 思路：维护一个动态窗口 [left, right]，允许窗口内包含最多 k 个 0。当右指针遇到 0 导致窗口内 0 的总数超过 k 时，收缩左边界 left。只有当 left 移出一个 0 后，窗口才重新获得翻转名额。在整个过程中，记录窗口达到的最大长度
        ans = 0
        turn_cnt = 0 # 反转次数
        left = 0
        for right, x in enumerate(nums):
            if x == 0 :
                turn_cnt += 1
            while turn_cnt > k : #此时必须收缩左边界
                if nums[left] == 0:
                     turn_cnt -= 1 # 移出一个0，计数才减1
                left += 1 # 左指针移动
            ans = max(ans,right-left+1)
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
