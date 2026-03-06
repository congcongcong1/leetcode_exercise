"""
LeetCode [611]. [有效三角形的个数]

难度: [Medium]
链接: https://leetcode.cn/problems/valid-triangle-number/
标签: [数组, 双指针, 排序]

题目描述:
    给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。
"""

from typing import List, Optional


class Solution:
   def triangleNumber(self, nums: List[int]) -> int:
        """
        解法一:逆序+ 相向双指针 枚举最长边

        思路:
            首先看到这个题目，可以想到这和之前的三数之和、四数之和的解法是类似的，限制条件是三角形任意两边之和不能大于第三边，
            而且是可以重复的，转化为代码就是：对于数组nums，nums[i],nums[j],nums[k]三个数可以组成三角形，那么一定满足：
            nums[i]+nums[j]>nums[k]
            nums[i]+nums[k]>nums[j]
            nums[j]+nums[k]>nums[i]
            或者是min(nums[i],nums[j],nums[k]) + mid > max(nums[i],nums[j],nums[k])
            考虑一些优化剪枝操作的话，如果nums[i]+nums[j]<=nums[k]，那么就可以直接continue
            最后返回三元组个数cnt
            1. ...对数组进行排序
            2. ...使用双指针移动法
            3. ...最后针对运行时间复杂度进行一些优化剪枝优化操作（加一些前置判断）

        时间复杂度: O(n^2+nlogn)
        空间复杂度: O(1)
        """
        nums.sort()
        ans = 0
        for k in range(len(nums) - 1, 1, -1):#倒序处理为了优化一退出循环
            c = nums[k]
            if nums[0] + nums[1] > c:  # 优化一
                ans += (k + 1) * k * (k - 1) // 6
                break
            if nums[k - 2] + nums[k - 1] <= c:  # 优化二
                continue
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    ans += j - i
                    j -= 1
                else:
                    i += 1
        return ans
        

# #用枚举短边的做法：同向双指针
#     def triangleNumber2(self, nums: List[int]) -> int:
#             """
#         解法二:正序+ 同向双指针 枚举最短边

#         思路:
#             首先看到这个题目，可以想到这和之前的三数之和、四数之和的解法是类似的，限制条件是三角形任意两边之和不能大于第三边，
#             而且是可以重复的，转化为代码就是：对于数组nums，nums[i],nums[j],nums[k]三个数可以组成三角形，那么一定满足：
#             nums[i]+nums[j]>nums[k]
#             nums[i]+nums[k]>nums[j]
#             nums[j]+nums[k]>nums[i]
#             或者是min(nums[i],nums[j],nums[k]) + mid > max(nums[i],nums[j],nums[k])
#             考虑一些优化剪枝操作的话，如果nums[i]+nums[j]<=nums[k]，那么就可以直接continue
#             最后返回三元组个数cnt
#             1. ...对数组进行排序
#             2. ...使用双指针移动法
#             3. ...最后针对运行时间复杂度进行一些优化剪枝优化操作（加一些前置判断）

#         时间复杂度: O(n^2+nlogn)
#         空间复杂度: O(1)
#         """
#         nums.sort()
#         n = len(nums)
#         ans = 0 
#         for i in range(n-2):
#             x = nums[i]
#             if x == 0: continue
#             j = i + 1
#             for k in range (j+1,n):
#                 while nums[k] - nums [j] >= x:
#                     j += 1
#                 ans += k-j
#         return ans
            




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
