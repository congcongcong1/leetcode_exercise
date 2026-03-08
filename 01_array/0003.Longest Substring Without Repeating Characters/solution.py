"""
LeetCode [3]. [无重复字符的最长子串]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/
标签: [数组, 双指针, 排序]

题目描述:
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""

from typing import List, Optional


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #思路：还是可以想到维护双指针的滑动窗口做法，
        # 如果left和right之间有重复字符就不断移动left直到没有， 
        # 关键在于如何处理重复字符这个问题，想到利用Hash表来解决，其中key为ch value为int 即该字符出现字数
        # 时间复杂度o(n) 空间复杂度o(128)
        ans = 0
        left = 0
        cnt = Counter() #hashmap char int   专门用于计数的hashmap
        for right,x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1: #当窗口内有重复字母
                cnt[s[left]] -= 1 #移除左端点字母
                left += 1 #缩小窗口
            ans = max(ans, right -left+1) # 更新窗口最大值
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
