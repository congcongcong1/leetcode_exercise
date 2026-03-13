"""
LeetCode 34. Find First and Last Position of Element in Sorted Array (二分查找)

难度: Medium
链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
标签: 二分查找，数组

题目描述:
    给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

    如果数组中不存在目标值 target，返回 [-1, -1]。

    你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""

from typing import List


class Solution:
    # 解法一  闭区间解法
     # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left
    
    # 解法二  开区间解法
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)  # 开区间 (left,right)
        while left +1 < right:  # 区间不为空 结束条件 left + 1 = right
            # 循环不变量：
            # nums[left] < target
            # nums[right] >= target
            mid = left +(right-left)//2 #防止溢出
            if nums[mid] >= target:
                right = mid   # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        # 循环结束后 left + 1 = right
        # 此时 nums[left] < target 而 nums[right] >= target
        # 所以 right 就是第一个 >= target 的元素下标
        return right    

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #思路：由于数组有序，且要求时间复杂度是O(logn) 所以用二分查找
        #开始位置start 即求x>=target的起始坐标（可能包含大于所以要先判断）
        # 结束位置end 即求 x<=target的最后一个数，转化为x >= target +1  的起始坐标的左边 （因为是有序的）
            start = self.lower_bound(nums,target)
            if start == len(nums) or nums[start] != target :  #全部都小于target，或者没有target存在
                return [-1,-1]
            end = self.lower_bound(nums,target+1)-1 # 求x<=target的最后一个数的坐标
            return [start,end]

    def search(self, nums: List[int], target: int) -> int:
        """
        解法二: 左闭右开 [left, right)

        思路:
            在 [left, right) 区间内查找，while left < right

        时间复杂度: O(log n)
        空间复杂度: O(1)
        """
        left, right = 0, len(nums)

        while left < right:  # [left, right) 区间有效条件
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # target 在 [mid+1, right)
            else:
                right = mid      # target 在 [left, mid)

        return -1


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
