"""
LeetCode [240]. [搜索二维矩阵 II]

难度: [Medium]
链接: https://leetcode.cn/problems/set-matrix-zeroes/   
标签: [数组, 矩阵]

题目描述:
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target.该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""

from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 每次比较target和矩阵右上角的值matrix[0][n-1],如果右上角的值大于target，那么最后一列的其他数可以都排除
        # 如果右上角的值小于target，那么第一行的其他数也都可以排除
        # 在剩余矩阵中继续重复该操作，直到找到target
        # 利用O(1)的时间获取了O(m)或者O(n)的信息，这就是时间复杂度O(m+n)的原因
        # 空间复杂度也是O(1)
        m, n = len(matrix),len(matrix[0])
        i, j = 0 , n-1
        while i < m and j >= 0 : #还有剩余元素
            if matrix[i][j] == target :
                return True
            if matrix[i][j] < target : #排除这一行
                i += 1
            else : #排除这一列
                j -= 1
        return False
        




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
