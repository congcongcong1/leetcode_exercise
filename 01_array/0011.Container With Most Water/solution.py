"""
LeetCode [11]. [盛最多水的容器]

难度: [Medium]
链接: https://leetcode.cn/problems/container-with-most-water/
标签: [数组, 双指针, 排序]

题目描述:
    给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    返回容器可以储存的最大水量。
    说明：你不能倾斜容器。
"""

from typing import List, Optional


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        解法一:双指针+ 短板效应

        思路:
            1. ...首先这题不能用排序的思想来做，因为涉及到H*W，但是可以尝试用双指针的思想
            2. ...双指针移动时，永远都是优先考虑短板，如果短板不移动，那么水永远不可能比上次多
            3. ...

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        # 思考：首先这题不能用排序的思想来做，因为涉及到H*W，但是可以尝试用双指针的思想
        #双指针移动时，永远都是优先考虑短板，如果短板不移动，那么水永远不可能比上次多
        #如何更深度理解呢？如果已经确定了一个最大的面积，那么短的边无论在中间怎么移动那么都不会增大面积，这就是短板效应
        n = len(height)
        current_area = 0
        max_area = 0
        i, j =0 , n-1
        while i < j:
            x, y = height[i],height[j]
            current_area = min(x,y)*(j-i)
            max_area = max(current_area, max_area)
            if x <= y:
                i += 1
            else :
                j -= 1            
        return max_area
            

    def solve_v2(self, nums: List[int]) -> int:
        """
        解法二: [解法名称，如 哈希表优化]

        思路:
            [描述你的思路]

        时间复杂度: O(?)
        空间复杂度: O(?)
        """
        pass


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
