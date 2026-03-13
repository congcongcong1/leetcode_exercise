"""
LeetCode [73]. [矩阵置零]

难度: [Medium]
链接: https://leetcode.cn/problems/set-matrix-zeroes/   
标签: [数组, 矩阵]

题目描述:
给定一个 m x n 的整数矩阵 matrix ，如果一个元素为 0 ，则将其整个行和列都设置为 0 ；
请使用 原地 算法。
"""

from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 原地算法指的是引入的辅助空间复杂度时O(1),就是在原矩阵上进行操作
        # 题目的意思就是如果i行有0，或者j列有0，那么令matrix[i][j] = 0
        # 方法一：使用额外的数组来记录
        # 时间复杂度O(mn) 空间复杂度O(m+n)
        # rowHasZero记录每一行是否包含0 colHasZero记录每一列是否包含0
        row_has_zero = [0 in row for row in matrix] #行是否包含0 ep:[true,false,true]
        col_has_zero = [0 in col for col in zip(*matrix)]  #行是否包含0 ep=:[false,true,false] *拆散集合，zip为并行遍历
        for i,row0 in enumerate(row_has_zero):
            for j , col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 原地算法指的是引入的辅助空间复杂度时O(1),就是在原矩阵上进行操作
        # 题目的意思就是如果i行有0，或者j列有0，那么令matrix[i][j] = 0
        # 方法二：不使用额外数组
        # 时间复杂度O(mn) 空间复杂度O(1)
        # 用矩阵的第一行和第一列来记录这一行或者这一列中是否有0，但是这会不可避免地会遇到第一行和第一列是否应该置为0的问题，所以在最开始就用两个额外的布尔变量来记录第一行和第一列是否包含0，如果第一行或者第一列一开始就包含0，那么就把第一行和第一列最后全部变成0，另外遍历时可以不用遍历第一行和第一列
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0] # 记录第一行是否包含0
        first_col_has_zero = any(row[0] == 0 for row in matrix) #记录第一列是否包含0

        #逐行逐列检查是否包含0
        #用第一列matrix[i][0]保存 row_has_zero[i]
        #用第一行matrix[0][j]保存 col_has_zero[j]
        for i in range(1,m):#无需遍历第一行
            for j in range(1,n): #无需遍历第一列
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):# 跳过第一行在最后修改
            for j in range(1,n):# 跳过第一列在最后修改
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] = 0
        
        # 最后处理第一行和第一列
        # 如果第一行在一开始就包含0，那么就把第一行全部变为0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        #如果第一列在一开始就包含0，那么就把第一列全部变为0
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
        




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
