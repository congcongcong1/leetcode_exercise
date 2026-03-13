"""
LeetCode [41]. [缺失的第一个正数]

难度: [Hard]
链接: https://leetcode.cn/problems/first-missing-positive/   
标签: [数组, 哈希表]

题目描述:
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""

from typing import List, Optional


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 题目要求: 时间复杂度O(n) 空间复杂度O(1)
        # 很明显是不能排序的，先考虑用set，因为它的查找复杂度是O(1) 但是最坏情况下空间复杂度是O(n),也不符合条件
        # 核心算法思路：原地哈希 (In-place Hash)的思想，把原数组nums想象成一排带编号的抽屉，规则：数字1必须被放入nums[0],数字2应该被放入nums[1]，依次类推，数字n应该被放入nums[n-1]
        # 然后遍历数组，如果发现nums[i]上放的数字不对，那么就该把他放到应有的位置上去
        # 那么如果有重复元素怎么办？ 比如nums[1] = 1 但是此时数字1已经被放入了nums[0]，此时我们必须忽略这一项，该怎么做呢，注意到可以用nums[nums[0]]==nums[1] 来避免交换，也就是需要检查nums[nums[i]-1]和nums[i]是否相等  而正确的位置都应该有nums[i] = i+1
        n = len(nums)
        
        for i in range(n):
            #只要nums[i] 他在 [1,n]的范围内，并且没有在正确的位置上(nums[nums[i]-1]),就要交换位置
            while 1<= nums[i]<=n and nums[i] != nums[nums[i]-1]:
                # 交换nums[i]和nums[nums[i]-1]
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        # 防止完毕后，第一个位置不对的就是答案
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 如果全部在位，那么返回n + 1
        return n + 1




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
