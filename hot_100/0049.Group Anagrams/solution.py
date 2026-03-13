"""
LeetCode 49. 字母异位词分组

难度: Easy
链接: https://leetcode.cn/problems/two-sum/
标签: - 数组
    - 哈希表
    - 字符串
    - 排序

题目描述:
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 思路：字母异位词即重新排列可以形成彼此，那么就是他们排序后是一摸一样的，可以作为key
        # 那么就可以维护一个hash表，{key:["aet","eat","tea"]}，每次有字符串加进来就可以按照key加入不同的列表
        # 确定hash表那么就需要确定一个唯一的键值，让同一组的值也能映射到这个key上，从而组成一个列表
        # 时间复杂度 O(knlogn) 空间复杂度O(kn)
        str_hash = defaultdict(list) # {}
        for s in strs :
            # 对字符串进行排序，形成唯一的key
            # sorted("eat")返回['a','e','t']
            key = "".join(sorted(s))  # nlogn
            str_hash[key].append(s)
        return list(str_hash.values())


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
