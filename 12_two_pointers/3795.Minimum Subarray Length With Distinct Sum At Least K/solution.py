"""
LeetCode [3795]. [不同元素和至少为 K 的最短子数组长度]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
给你一个整数数组 nums 和一个整数 k。

返回一个 子数组 的 最小 长度，使得该子数组中出现的 不同 值之和（每个值只计算一次）至少 为 k。
如果不存在这样的子数组，则返回 -1。

子数组 是数组中一个连续的 非空 元素序列。
"""

from typing import List, Optional



class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
      # 思路：翻译一下题目的意思：在一个连续数组中找到一个最小子数组的非重复元素的和至少为k,
      #重复元素就要想到用哈希表来维护每个元素出现的次数
        left = 0
        ans = inf
        s = 0
        cnt =defaultdict(int)
        if sum(nums) < k : return -1
        for right,x in enumerate(nums):
            cnt[x] += 1
            if cnt[x] ==1:
                s += x
            while s >= k :#如果已经满足条件了，那么现在需要移动左指针，但是也要移动非重复的元素来减少和
                ans = min(ans,right-left+1)
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    s -= nums[left]
                left += 1
        return ans if ans <inf else -1




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
