"""
LeetCode 438. 找到字符串中所有字母异位词

难度: Medium
链接: https://leetcode.cn/problems/two-sum/
标签: - hash表 字符串 滑动窗口

题目描述:
给定两个字符串 s 和 p ，找到 s 中所有 p 的字母异位词的子串，返回这些子串的起始索引。你可以按 任意顺序 返回答案。

字母异位词 指的是在两个字符串中，每种字母出现次数相同。例如，"abc" 和 "bca" 互为字母异位词。
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 查找子字符串，可以想到用滑动窗口:分为定长滑动窗口和不定长滑动窗口
        # while的单调条件：只要不是字母异位词就可以一直移动left，而且left和right之间可以差2,因为要三个字符才行
        # 怎么判断是否为字母异位词？可以用一个hash表或者直接用Counter来统计每种字母出现的次数 {a:1,b:2,c:3}
        # 如果子字符串中和p每种字母出现次数都相等，那么就是字母异位词，反之则不断移动left，来满足条件
        # 先用定长滑动窗口：枚举 s 的所有长为 n 的子串 t，如果 t 的每种字母的出现次数，和 p 的每种字母的出现次数都相同，那么 t 是 p 的异位词
        # 时间复杂度：O(Σn+m) Σ为字符集合大小 Σ<= 26
        # 若要将时间复杂度进行优化，那么就是不要比较出现的次数相等，而是统计种类，每次比较种类即可时间复杂度是O(1)
        # 空间复杂度O(∣Σ∣)
        cnt_p = Counter(p) #统计p中每个字符出现的次数,遍历字符串，耗时O(m)
        cnt_s = Counter()    #统计s的长为len(p)的子字符串t中字符出现的次数
        ans = []

        for right,c in enumerate(s): # 总耗时O(Σn)
            cnt_s[c] += 1 # 时间复杂度O(1)

            left = right -len(p) + 1 # [left,right] len(p) = right - left + 1 定长窗口
            if left < 0:  # 即长度没有p,那么继续外层循环
                continue

            if cnt_s == cnt_p : #如果t和p中每种字符出现的次数都相等,比较耗时O(Σ),Σ为字符串中最多的字母个数，小于26
                ans.append(left) #左端点left加入答案list #
            
            cnt_s[s[left]] -= 1 #左端点字母离开窗口 因为是定长的 耗时O(1)
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
