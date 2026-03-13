"""
LeetCode 2300. Successful Pairs of Spells and Potions (咒语和药水的成功对数)

难度: Medium
链接: https://leetcode.cn/problems/binary-search/
标签: 二分查找

题目描述:
给你两个正整数数组 spells 和 potions ，按 非递减顺序 排列。只有当两个数组中元素相乘大于等于某个阈值时，咒语和药水才算成对成功。
返回一个长度与 spells 相等的整数数组 answer ，其中 answer[i] 是能与第 i 个咒语配对成功的药水数目。
"""

from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 题目分析：可以将potions进行sort排序，时间复杂度O(nlogn)，比起遍历O(n^2)会好一点
        # 然后对于每一个spells[i] ,查找对应的potions中 x >= success/spells[i],可以用bisect.left()
        # 时间复杂度：O(nlogn+mlogm) 空间复杂度：O(1)
        potions.sort()
        pairs = [0]*len(spells)
        for i, x in enumerate(spells): #x = spells[i]
            pairs[i] = len(potions)-bisect_left(potions,success/spells[i])
        return pairs

# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1: 目标值在数组中
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4, "测试用例 1 失败"

    # 测试用例 2: 目标值不在数组中
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1, "测试用例 2 失败"

    # 测试用例 3: 单元素数组
    assert sol.search([5], 5) == 0, "测试用例 3 失败"

    # 测试用例 4: 单元素，未找到
    assert sol.search([5], -5) == -1, "测试用例 4 失败"

    # 两种写法交叉验证
    assert sol.search_closed([-1, 0, 3, 5, 9, 12], 9) == 4, "左闭右闭 验证失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
