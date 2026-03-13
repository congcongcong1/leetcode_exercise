"""
LeetCode [11]. [盛最多水的容器]

难度: [Medium]
链接: https://leetcode.cn/problems/container-with-most-water/
标签: [数组, 双指针, 贪心]

题目描述:
    给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。
    说明：你不能倾斜容器。
"""

from typing import List, Optional


class Solution:
        def maxArea(self, height: List[int]) -> int:
        # 思考：首先这个题目肯定是要用相向双指针移动来解决，关键是双指针移动的条件是什么
        # 如果已经确定了一对指针left和right，此时他们维护的面积最大，此时要移动，如果不移动短板，那么再怎么往中间移动移动水都不会比上次多，所以短板应该向右边移动
        # 时间复杂度O(n) :用了缩减搜索空间的思想，每排除一根柱子那么就可以排除一行以及一列的搜索空间
        # 空间复杂度O(1)
            left, right = 0 ,len(height)-1
            ans = 0
            while left < right : 
                current_area = min(height[left],height[right])*(right-left)
                ans = max(ans,current_area)
                if height[left] < height[right]:
                    left += 1
                else :
                    right -= 1
            return ans


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1
    assert sol.solve([]) == None, "测试用例 1 失败"

    # 测试用例 2
    assert sol.solve([]) == None, "测试用例 2 失败"

    # 边界case
    # assert sol.solve([]) == None, "边界case 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
