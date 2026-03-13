"""
LeetCode 875. Koko Eating Bananas (爱吃香蕉的珂珂)

难度: Medium
链接: https://leetcode.cn/problems/koko-eating-bananas/
标签: 二分查找

题目描述:
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。 

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 这是一个二分查找的转换题目，也就是要求k，那么k要满足一个怎么样的关系式才移动左右指针呢？
        # 注意到吃完一香蕉需要⌈p/k⌉ (上取整) = [p-1//k]+1 下取整 根据这个公式，只要满足所有的香蕉堆时间耗时加起来小于h就行  采用开区间的二分查找，
        # 时间复杂度：O(nlogU) U为piles的最大值
        # 空间复杂度：O(1)
        left, right = 0, max(piles) #左区间一定不能，右区间一定能
        while left + 1 < right : #退出循环的条件：left+1 = right
            mid = left + (right - left)//2
            if sum((x-1)//mid  for x in piles) <= h - len(piles): #如果满足要求，那么继续在(left,mid)中找
                right = mid
            else :
                left = mid
        return right

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
