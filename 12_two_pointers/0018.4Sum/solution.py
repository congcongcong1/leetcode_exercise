"""
LeetCode [18]. [四数之和]

难度: [Medium]
链接: https://leetcode.cn/problems/4sum/
标签: [数组, 双指针, 排序]

题目描述:
    给你一个整数数组 nums ，判断是否存在四元组 [nums[i], nums[j], nums[k], nums[l]] 满足 i != j、i != k 、i != l、j != k、j != l、k != l ，同时还满足 nums[i] + nums[j] + nums[k] + nums[l] == 0 。请你返回所有和为 0 且不重复的四元组。
    注意：答案中不可以包含重复的四元组。
"""

from typing import List, Optional


class Solution:
   def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        解法一:首先这种题目先对数组进行排序，然后使用双指针法，可以将四数之和两次转化为双数之和，然后再用双指针法降低时间复杂度

        思路:
            1. ...对数组进行排序
            2. ...使用双指针法，将三数之和转化为双数之和，然后再用双指针法降低时间复杂度
            3. ...由于不能包含重复的三元组，所以如果下一个数和当前的数相同，那么就应该跳过，使用while可以跳过多次

        时间复杂度: O(n^3)
        空间复杂度: O(1)
        """
        nums.sort()
        n = len(nums)
        res = []
        for a in range(n-3):
            # 对a进行剪枝操作以及不重复优化操作
            x = nums[a]
            if  a > 0 and x == nums[a-1] : continue
            if  x + nums[a+1] + nums[a+2] + nums[a+3] > target : break
            if  x + nums [-1] + nums[-2] + nums[-3] < target : continue
            for b in range(a+1,n-2):
                y = nums[b]
                # 对b进行剪枝操作以及不重复优化操作
                if b > a + 1 and y ==nums[b-1] :continue
                if x + y + nums[b+1] + nums[b+2] > target : break
                if x + y + nums[-1] + nums[-2] < target : continue
                #进行双指针
                c , d = b+1, n-1
                while c < d:
                    sum = x + y + nums[c] + nums[d]
                    if sum < target: c += 1
                    elif sum > target: d -= 1
                    else:
                        res.append([x,y,nums[c],nums[d]])
                        #为了避免c，d重复
                        c += 1
                        while c < d and nums[c] == nums[c-1]: c += 1
                        d -= 1
                        while c < d and nums[d] == nums[d+1]: d -= 1
        return res





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
