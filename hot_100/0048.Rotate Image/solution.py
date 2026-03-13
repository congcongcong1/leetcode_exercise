"""
LeetCode [48]. [旋转图像]

难度: [Medium]
链接: https://leetcode.cn/problems/spiral-matrix/   
标签: [数组, 矩阵]

题目描述:
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像
"""

from typing import List, Optional

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转矩阵 :从行列分开分析来找到对应位置元素的变换公式
        # 分析：第j列的元素去往了第j行
        # 第i行的元素去了第n-1-i列
        # 所以(i,j) -> （j,n-1-i)
        # (i,j)->(转置)->(j,i)->行翻转->(j,n-1-i)
        # 时间复杂度O(n^2) 空间复杂度 O(1)
        n = len(matrix)
        # 第一步：转置
        for i in range(n):
            for j in range(i): #遍历对角线以下的函数
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # 第二步：行翻转(左右翻转)    #上下翻转：matrix.reverse()
        for row in matrix:
            row.reverse()
        




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
