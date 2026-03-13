"""
LeetCode 2529. Maximum Count of Positive Integer and Negative Integer (正整数和负整数的最大计数)

难度: Easy
链接: https://leetcode.cn/problems/binary-search/
标签: 二分查找

题目描述:
给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。
"""

from typing import List


class Solution:

    def lower_bound(self,nums:List[int],target:int) -> int :
        left,right = -1, len(nums) #(left,right)
        while left + 1 < right :# stop while left + 1 = right
            mid = left +(right-left)//2 # avoid overload
            # 循环不变量： nums[left] < target  nums[right] >= target
            if nums[mid] >= target:
                right = mid # to (left,mid)
            else :
                left = mid  # to (mid,right)
        # while stop : left + 1 = right, nums[right] >= target
        return right
        
    #方法一：手写查找函数
    def maximumCount(self, nums: List[int]) -> int:
        # 思路：首先是有序单调数组，是标准的二分查找题目，而且可以转变成：
        # target 为 0  求正整数数目 pos：先求x>target的第一个起始坐标 然后再求数目
        # 求负整数数目neg：先求x<target 的最后一个起始坐标，然后再求数目即可 
        # 时间复杂度o(logn)
        pos_start = self.lower_bound(nums,1)
        pos = len(nums) - pos_start
        neg_end = self.lower_bound(nums,0) - 1
        neg = neg_end + 1
        return max(pos,neg)

    # 方法二：用自带函数bisect_left和bisect_right ：分别是：找到第一个大于等于的位置，找到第一个大于的位置
    def maximumCount(self, nums: List[int]) -> int:
        
        neg = bisect_left(nums, 0) # 找到第一个大于等于0的位置
        pos = len(nums) - bisect_right(nums, 0)  #bisect_right(nums, 0) 找到第一个大于0的位置
        return max(neg, pos)


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
