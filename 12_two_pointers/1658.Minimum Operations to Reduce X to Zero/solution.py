"""
LeetCode [1658]. [将 x 减到 0 的最小操作数]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
给你一个整数数组 nums 和一个整数 x 。每一次操作时，
你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。
请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。
"""

from typing import List, Optional



class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 逆向思维，用正难则反的思想，问题可以被转化为求最长子数组的和恰好等于sum(nums)-x,用滑动窗口解决
        ans = -1 
        left = 0
        target = sum(nums)- x
        if target < 0: return -1
        s = 0
        for right, x in enumerate(nums):
            s += x
            while  s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans,right-left+1)
        return -1 if ans < 0 else len(nums) - ans




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
