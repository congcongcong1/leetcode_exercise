"""
LeetCode 2080. Range Frequency Queries (区间内查询数字的频率)

难度: Medium
链接: https://leetcode.cn/problems/range-frequency-queries/
标签: 二分查找，哈希表

题目描述:
请你设计一个数据结构，它能求出给定子数组内一个给定值的 频率。
子数组中一个值的 频率 指的是这个子数组中这个值的出现次数。
请你实现 RangeFreqQuery 类：
RangeFreqQuery(int[] arr) 用下标从 0 开始的整数数组 arr 构造一个类的实例。
int query(int left, int right, int value) 返回子数组 arr[left...right] 中 value 的 频率。
一个 子数组 指的是数组中一段连续的元素。arr[left...right] 指的是 nums 中包含下标 left 和 right 在内 的中间一段连续元素。
"""

from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        pos_hash = defaultdict(list) # 记录每个值出现的下标
        for i, x in enumerate(arr):
            pos_hash[x].append(i) # {10:[0,2,4],20:[1,3],30:[5]}
        self.pos = pos_hash
        

    def query(self, left: int, right: int, value: int) -> int:
        # 给定值的频率可以用hashmap 复杂度是o(n)
        #  也可以用二分查找，先排序，复杂度是O(logn+Q*nlogn) 这会导致超时
        # 先用二分查找实现:在给定子数组内排序，先找到大于target的下标，再找到小于target的下标
        # 所以必须先用hashmap存储一下arr[left,right]中每个元素出现的频率
        # 对于arr中每一个数，计算他在arr中出现位置的下标，这个下标是天然有序的，那么题目就转变为了下标列表中，满足left<= i <= right的下标i的个数，对于下标数组可以用二分查找法快速求出[left,right-1] 
        # 时间复杂度：O(n+Q*logn) Q为查询的次数
        # 空间复杂度：O(n) 声明了hashmap
        idx = self.pos[value] # 获取对应的value下标数组
        return bisect_right(idx,right) - bisect_left(idx,left)

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
