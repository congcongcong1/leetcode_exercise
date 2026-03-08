"""
LeetCode [3090]. [每个字符最多出现两次的最长子字符串]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
给定一个字符串 s ，请你找出其中每个字符最多出现两次的 最长 子串 的长度。
"""

from typing import List, Optional


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # 用滑动窗口来维护这个字符串，枚举右指针，字符出现次数用hashmap统计，
        # 当有字符出现两次以上就减去左指针，并且右移
        # 时间复杂度 O(n) 空间复杂度O(1)
        ans = 0
        left = 0
        cnt = defaultdict(int) # hashmap char int
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2: # 当有字符出现两次以上
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
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
