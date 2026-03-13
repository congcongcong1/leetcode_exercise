"""
LeetCode 128. 最长连续序列

难度: Medium
链接: https://leetcode.cn/problems/two-sum/
标签: - 数组
    - 哈希表
    - 字符串
    - 排序

题目描述:
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 时间复杂度O(n)，那么肯定不能进行排序nlogn，要对无序的数组进行操作，
        #核心思路：对于 nums 中的元素 x，以 x 为起点，不断查找下一个数 x+1,x+2,⋯ 是否在 nums 中，并统计序列的长度
        #为了做到 O(n) 的时间复杂度，需要两个关键优化：1 把 nums 中的数都放入一个哈希集合中，这样可以 O(1) 判断数字是否在 nums 中。2 如果 x−1 在哈希集合中，则不以 x 为起点。为什么？因为以 x−1 为起点计算出的序列长度
        # 优化，如果其中一个最长序列已经是m/2了，那么就不用管再继续查找了，因为最长也不会超过m/2
        # 时间复杂度 O(n) : 每个元素最多执行两条语句
        # 空间复杂度 O(m)： m是nums中不同元素个数，用于开辟num_set
        num_set = set(nums) #转化为set 无序、不重复的元素容器 例如 {1，2，3，4，0} 
        max_length = 0
        current_length = 0
        for num in num_set: # 要遍历hash集合，而不是nums！
            if (num - 1)  in num_set : # 如果num-1不在set里，就以num为起点，否则没意义   时间复杂度O(1),如果不用set 那么就是O(n)
                continue
            current_num = num # 当前起点
            current_length = 1 # 目前的连续长度
            while (current_num + 1) in num_set: 
                current_length += 1
                current_num += 1
            max_length = max(max_length,current_length)
            if max_length > len(num_set)//2:#  优化，如果其中一个最长序列已经是m/2了，那么就不用管再继续查找了，因为最长也不会超过m/2
                break
        return max_length


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    # 测试用例 1: 基础情况
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1], "测试用例 1 失败"

    # 测试用例 2: 答案在数组中间
    assert sol.twoSum([3, 2, 4], 6) == [1, 2], "测试用例 2 失败"

    # 测试用例 3: 相同元素
    assert sol.twoSum([3, 3], 6) == [0, 1], "测试用例 3 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
