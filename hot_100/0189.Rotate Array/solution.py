"""
LeetCode [189]. [轮转数组]

难度: [Medium]
链接: https://leetcode.cn/problems/rotate-array/   
标签: [数组, 双指针, 排序]

题目描述:
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
"""

from typing import List, Optional


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：第一想法是用队列来实现
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        nums_q = deque(nums) # 初始化双端队列
        n = len(nums)
        for i in range (k%n):#执行k%n次
            x = nums_q[-1]
            nums_q.pop()
            nums_q.appendleft(x)

        # 将结果写回原数组 nums
        for i in range(n):
            nums[i] = nums_q[i]


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：因为空间复杂度是O(1),所以不能使用切片，队列的方式
        # 下面记录一种翻转的方式，不需要引入额外的空间
        # 先翻转整个数组，再反转前k个，再反转后n-k个即可得到
        # 把一个子数组反转两次，子数组的元素顺序不变
        # 时间复杂度O(n)
        # 空间复杂度O(1)
        def reverse(i:int, j: int) -> None:
            while i < j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        
        n = len(nums)
        k %= n # 轮转的次数
        reverse(0,n-1) # 翻转整个数组
        reverse(0,k-1) # 翻转前k项
        reverse(k,n-1) # 翻转后n-k项

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 思路：切片的方式
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        n = len(nums)
        k %= n
        if k > 0:
            nums[:] = nums[-k:] + nums[:-k]




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
