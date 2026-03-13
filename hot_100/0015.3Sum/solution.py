"""
LeetCode [15]. [三数之和]

难度: [Medium]
链接: https://leetcode.cn/problems/3sum/
标签: [数组, 双指针, 排序]

题目描述:
    给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
"""

from typing import List, Optional


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        解法一:首先这种题目先对数组进行排序，然后使用双指针法，可以将三数之和转化为双数之和，然后再用双指针法降低时间复杂度

        思路:
            1. ...对数组进行排序
            2. ...使用双指针法，将三数之和转化为双数之和，然后再用双指针法降低时间复杂度
            3. ...由于不能包含重复的三元组，所以如果下一个数和当前的数相同，那么就应该跳过，使用while可以跳过多次

        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        # 规定 i < j < k(题目没有给就自己规定)
        nums.sort() #先排序
        n = len(nums)
        ans = []
        for i in range (n-2):
            x =nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue #跳过本次
            if nums[i] + nums[i+1] + nums[i+2] > 0 :
                break #如果第一个数加上第二个数加上第三个数大于0，那么三数之和不可能为0
            j = i + 1 #左指针
            k = n - 1 #右指针
            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1 #右指针左移
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1 #左指针右移
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        
        return ans
            

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
