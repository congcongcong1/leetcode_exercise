"""
LeetCode [16]. [最接近的三数之和]

难度: [Medium]
链接: https://leetcode.cn/problems/3sum-closest/
标签: [数组, 双指针, 排序]

题目描述:
    给你一个长度为 n 的整数数组 nums 和 一个目标值 target。
    请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近
    返回这三个数的和
"""

from typing import List, Optional


class Solution:
   def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        解法一:排序+双指针

        思路:
            1. ...对数组进行排序
            2. ...使用双指针移动法
            3. ...最后针对运行时间复杂度进行一些优化剪枝优化操作（加一些前置判断）

        时间复杂度: O(n^2+nlogn)
        空间复杂度: O(1)
        """
        # 规定 i < j < k(题目没有给就自己规定)
        nums.sort() #先排序
        n = len(nums)
        ans = inf


        for i in range(n-2):
        #增加一些剪枝操作来优化时间
        # 首先是 如果下一个数字和当前的数字重复那么直接跳过这个数字
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
        # 第二种情况如果当前数和最相邻的两个最小数都大于target，那么直接返回当前值即可
            if nums[i] + nums[i+1] + nums[i+2] > target:
                if abs(nums[i] + nums[i+1] + nums[i+2]-target) <abs(ans-target):
                    ans = nums[i] + nums[i+1] + nums[i+2]
                    return ans
        
        # 第三种情况如果当前数和最大的两个数都小于target，那么可以跳过这次，继续循环
            if nums[i] + nums[-1] + nums[-2] < target:
                if abs(nums[i] + nums[-1] + nums[-2]-target) <abs(ans-target):
                    ans = nums[i] + nums[-1] + nums[-2]
                    continue
            
            j = i+1;#左指针
            k = n-1;#右指针
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                elif s < target: #左指针右移
                    j += 1
                else: #右指针左移
                    k -= 1
                if  abs(s - target) < abs(ans - target):
                    ans = s
        
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
