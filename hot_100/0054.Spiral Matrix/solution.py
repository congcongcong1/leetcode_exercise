"""
LeetCode [54]. [螺旋矩阵]

难度: [Medium]
链接: https://leetcode.cn/problems/spiral-matrix/   
标签: [数组, 矩阵]

题目描述:
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""

from typing import List, Optional

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 螺旋矩阵：matrix[0][0]->matrix[0][-1] -> matrix[-1][-1]->matrix[-1][0] ->matrix[1][0]->matrix[1][-2]->matrix[-2][-2]^依次类推直到最后一个元素被返回完，现在需要找规律
        # 思路：边界模拟，维护上下左右四个边界，每次跑完就更新边界，如果边界重叠那么就结束
        # 初始化上下边界
        # 时间复杂度O(mn)
        # 空间复杂度O(1)
        top, bottom = 0,len(matrix) - 1
        left, right = 0 ,len(matrix[0]) - 1
        ans = []
        while True:
            # 1. 首先从左往右走
            for i in range(left,right+1): #[left,right]
                ans.append(matrix[top][i])
            top += 1 # 维护上边界
            if top > bottom : break # 检查是否重叠

            # 2. 然后从上往下走
            for i in range(top,bottom+1):#[top,bottom]
                ans.append(matrix[i][right])
            right -= 1 #维护左边界
            if left > right : break

             # 3. 然后从右往左走
            for i in range(right,left-1,-1):#逆序[right,left]
                ans.append(matrix[bottom][i])
            bottom -= 1 #维护下边界
            if top > bottom : break # 检查是否重叠         

             # 4. 最后从下往上走
            for i in range(bottom,top-1,-1):#逆序[bottom,tp[]]
                ans.append(matrix[i][left])
            left += 1 #维护左边界
            if left > right : break 
        return ans
        




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
