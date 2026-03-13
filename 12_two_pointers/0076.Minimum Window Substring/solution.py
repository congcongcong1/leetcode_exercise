"""
LeetCode [76]. [最小覆盖子串]

难度: [Hard]
链接: https://leetcode.cn/problems/minimum-window-substring/   
标签: [数组, 双指针, 排序]

题目描述:
给你一个字符串 s 和一个字符串 t ，请你找出 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

子数组 是数组中一个连续的非空元素序列。
"""

from typing import List, Optional



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 思路：包含重复字符，用滑动窗口解决最短子字符串问题，关键在于while的单调性如何写
        # 用hash表来统计t中每一个字符出现的次数，然后逐个在s中滑动窗口中验证
        # 1. 先统计 t，再计算种类
        #时间复杂度：O(n+m)
        #空间复杂度：O(128)
        cnt = defaultdict(int)  # 比 Counter 更快
        for c in t:
            cnt[c] += 1
        less = len(cnt)  # 有 less 种字母的出现次数 < t 中的字母出现次数

        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):  # 移动子串右端点
            cnt[c] -= 1  # 右端点字母移入子串
            if cnt[c] == 0:
                # 原来窗口内 c 的出现次数比 t 的少，现在一样多
                less -= 1
            while less == 0:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                x = s[left]  # 左端点字母
                if cnt[x] == 0:
                    # x 移出窗口之前，检查出现次数，
                    # 如果窗口内 x 的出现次数和 t 一样，
                    # 那么 x 移出窗口后，窗口内 x 的出现次数比 t 的少
                    less += 1
                cnt[x] += 1  # 左端点字母移出子串
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]





    def minWindow(self, s: str, t: str) -> str:
        # 思路：方法二用双指针方法，注意关键点是while单调性用cnt_s >cnt_t判断
        # 时间复杂度：O(n+128m)
        # 空间复杂度：O(128)
        # 1. 先统计 t，再计算种类
        cnt_s = Counter() #s字符串字母出现的次数
        cnt_t = Counter(t)#t字符串字母出现的次数

        ans_left, ans_right = -1,len(s)
        left = 0
        for right,ch in enumerate(s):
            cnt_s[ch] += 1
            while cnt_s >= cnt_t : #全部涵盖了
                if right - left < ans_right -ans_left: #更新起始位
                    ans_right, ans_left = right, left
                cnt_s[s[left]] -= 1
                left += 1
           
        return "" if ans_left <0  else s[ans_left : ans_right + 1]




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
