"""
LeetCode 560. 和为 K 的子数组

难度: Medium
链接: https://leetcode.cn/problems/two-sum/
标签: - hash表 数组 前缀和

题目描述:
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 思路：首先想到的是滑动窗口解决，但是没有单调性，也就是sum不会越来越大，不能用while解决
        # 对于连续子数组的求和问题，可以想到用前缀和来解决：任意子数组都是一个前缀去掉前缀后的结果。所以任意子数组的和，都可以表示为两个前缀和的差。规定前缀和数组，S[0]=0, S[i]=0+^+a[i-1]  S[i+1] = S[i]+a[i]
        # 子数组和为k，即[i,j-1]的子数组和为k，那么s[j]-s[i] = k 那么是不是转化成了两数之和的形式
        # 可以很容易想到用hash表来记录[s[i]:i,S[i+1]:i+1] ，然后查找s[j]-k 是否在hash表中，也就是枚举右寻找左
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)
        cnt = defaultdict(int) # {S[0]:1,}
        cnt[0] = 1
        s = 0
        ans = 0
        for x in nums:#枚举右，寻找左，同时记录前缀和以及hash表的信息
            s += x # s = S[j]
            ans += cnt[s - k]
            cnt[s] += 1
        return ans

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
