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
        # 思路：还是可以想到维护双指针的滑动窗口做法，如果left和right之间有重复字符就不断移动left直到没有， 关键在于如何处理重复字符这个问题，想到利用Hash表来解决，其中key为ch value为int 即该字符出现字数
        # 返回连续的字符串可以想到用滑动窗口，重复字符可以用hash表统计，while也有单调性
        # while单调性：右指针移动扩大字符串，当出现重复字符就移动左指针直到没有重复字符串位置
        # 时间复杂度O(n) left至多增加n次，所以整个二重循环多循环O(n)次
        # 空间复杂度O(128) 128为ASCII字符表的大小  
        left = 0
        ans = 0
        cnt_hash = defaultdict(int) #{a:1, b:1 ,c:1}
        for right,ch in enumerate(s):
            cnt_hash[ch] += 1
            while cnt_hash[ch] == 2:
                cnt_hash[s[left]] -= 1 #先移除左端字母
                left += 1        #再缩小窗口
            ans = max(ans,right - left + 1) #更新窗口最大值[left,right]
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        # 思路：还是可以想到维护双指针的滑动窗口做法，如果left和right之间有重复字符就不断移动left直到没有， 关键在于如何处理重复字符这个问题，想到利用Hash表来解决，其中key为ch value为int 即该字符出现字数
        # 返回连续的字符串可以想到用滑动窗口，重复字符可以用hash表或者set集合来做
        # while单调性：右指针移动扩大字符串，当出现重复字符就移动左指针直到没有重复字符串位置
        # 时间复杂度O(n) left至多增加n次，所以整个二重循环多循环O(n)次
        # 空间复杂度O(128) 128为ASCII字符表的大小 
        left = 0
        ans = 0
        window = set() #set记录无序不重复的字符串数组 查找o(1)
        for right,ch in enumerate(s):
            while ch in window:
                window.remove(s[left])
                left += 1
            window.add(ch)
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
