"""
LeetCode [2563]. [统计公平数对的数目]

难度: [Medium]
链接: https://leetcode.cn/problems/count-the-number-of-fair-pairs/ 
标签: [数组, 双指针, 排序]

题目描述:
给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。

如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：

0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper
"""

from typing import List, Optional


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 思想：可以先从小到大排序，因为返回的是数对的数目
        # 目前的想法是先遍历i,然后然后用二分查找求满足的j的数目
        # 时间复杂度： O(nlogn)
        # 空间复杂度： O(1)
        ans = 0
        nums.sort()
        for i, x in enumerate(nums):
            ans += bisect_right(nums,upper-x,i+1) - bisect_left(nums,lower-x,i+1) # 从下标i+1开始往后找 因为i < j
        return ans
    
        def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # 思想：可以先从小到大排序，因为返回的是数对的数目
        # 解法2：利用双指针，因为具有单调性可以用while，设计一个函数统计小于target和的数目，然后
        # func(upper) - func(lower-1)
        # 时间复杂度： O(nlogn)
        # 空间复杂度： O(1)
            nums.sort()
            def count(target:int) -> int:
                i, j = 0,len(nums)-1
                ans = 0
                while i < j :
                    if nums[i] + nums[j] <= target:
                        ans += j - i
                        i += 1
                    else:
                        j -= 1
                return ans
            return count(upper)-count(lower-1)




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
