"""
LeetCode [238]. [除自身以外数组的乘积]

难度: [Medium]
链接: https://leetcode.cn/problems/product-of-array-except-self/   
标签: [数组, 前缀和]

题目描述:
给你一个整数数组 nums,返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积。
题目数据保证数组 nums之中任意元素的全部前缀元素和后缀的乘积都在32位整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题
"""

from typing import List, Optional


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)的时间复杂度的要求，如果常规的遍历+查找的时间复杂度至少是O(n^2)
        # answer[i] = product(nums)//answer[i],题目要求不能用除法
        # 利用前缀和的思想，是不是可以用前缀积数组来实现
        # 维护一个前缀积和后缀积数组，那么answer[i] = 前缀积*后缀积
        # 时间复杂度 O(n)
        # 空间复杂度 O(n)
        n = len(nums)
        pre =[1] * n
        for i in range(1,n):#[1,n-1]
            pre[i] = pre[i-1]*nums[i-1]
        
        suf = [1]*n
        for i in range(n-2,-1,-1): # [n-2 -> 0]
            suf[i] = suf[i+1] *nums[i+1]
        
        return [p*s for p, s in zip(pre,suf)]




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
