"""
LeetCode [2962]. [统计最大元素出现至少 K 次的子数组]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 滑动窗口]

题目描述:
给你一个整数数组 nums 和一个整数 k，
请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
"""

from typing import List, Optional


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 思路：首先求出数组中的最大元素，然后依旧用双指针维护一个滑动窗口，
        # 枚举右指针，如果出现满足题目条件的假设出现的情况，此时要维护左指针，
        # 不断右移直到不满足题目中的条件为止，而对于答案，[left,right]不满足条件，
        # 但是[left-1,right]是满足条件的，所以ans += left
        ans = 0 
        left = 0 
        cnt = 0
        max_num = max(nums)
        for right, x in enumerate(nums):
            if x == max_num :
                cnt += 1
            while cnt == k :#如果这样的子数组已经出现，那么右移left来不符合条件
                if nums[left] == max_num:
                    cnt -= 1
                left += 1
            ans += left
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
