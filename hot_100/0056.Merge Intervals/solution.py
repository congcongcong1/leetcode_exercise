"""
LeetCode [56]. [合并区间]

难度: [Medium]
链接: https://leetcode.cn/problems/merge-intervals  
标签: [数组, 排序]

题目描述:
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

"""

from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 方法：按照列表的左端点排序
        # 首先如果能进行排序，那么合并区间就可以从左往右进行了，所以需要根据list内，每个数组第一个数进行排序
        # 时间复杂度O(nlogn) 时间瓶颈在排序上
        # 空间复杂度O(1)
        intervals.sort(key=lambda x: x[0]) # 只看每个列表中的第一个元素进行排序
        merged = []
        for interval in intervals :
            # 如果和前面已经合并了区间不重叠
            # 即如果merged为空，或者当前区间的start 大于 最后一个合并区间的end，那么直接添加interval区间
            if not merged or interval[0] >merged[-1][-1]:
                merged.append(interval)
            else: # 如果和前面区间发生了重叠
                merged[-1][-1] = max(interval[-1],merged[-1][-1])
        return merged




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
