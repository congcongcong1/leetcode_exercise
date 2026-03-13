"""
LeetCode [2730]. [找到最长的半重复子字符串]

难度: [Medium]
链接: https://leetcode.cn/problems/minimum-size-subarray-sum/   
标签: [数组, 双指针, 排序]

题目描述:
如果一个字符串 t 中至多有一对相邻字符是相等的，那么称这个字符串 t 是 半重复的 。
例如，"0010"、"002020"、"0123"、"2002" 和 "54944" 是半重复字符串，
而 "00101022"（相邻的相同数字对是 00 和 22）和 "1101234883"（相邻的相同数字对是 11 和 88）不是半重复字符串。

请你返回 s 中最长的 半重复 子字符串 的长度。
"""

from typing import List, Optional


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ## 思路： 用双指针维护一个滑动窗口，窗口内始终满足只有一对相邻字符相等，如果不相等，那么就移动左指针直到相等
        ans, left, same = 1, 0, 0
        for right in range(1, len(s)):
            same += s[right] == s[right - 1]
            if same > 1:  # same == 2
                left += 1
                while s[left] != s[left - 1]:
                    left += 1
                same = 1
            ans = max(ans, right - left + 1)
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
