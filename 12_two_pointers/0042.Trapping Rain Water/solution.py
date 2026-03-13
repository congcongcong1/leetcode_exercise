"""
LeetCode [42]. [接雨水]

难度: [Hard]
链接: https://leetcode.cn/problems/trapping-rain-water/
标签: [数组, 双指针, 排序]

题目描述:
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

    示例 1：
    输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
    输出：6
    解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

    示例 2：
    输入：height = [4,2,0,3,2,5]
    输出：9

    提示：
    n == height.length
    1 <= n <= 2 * 10^4
    0 <= height[i] <= 10^5
"""

from typing import List, Optional


class Solution:
    def trap(self, height: List[int]) -> int:
        #方法一：前后缀分解法
        #思路: 将每一个柱子视为一个存储容器，那么他的水容量取决于min(height[left],height[right])-柱子高度,所以记录最大前后缀即可（因为只要最大前后缀够高水是不会流出去的）
        #时间复杂度 o(n) 空间复杂度o(n)
        ans = 0
        n = len(height)
        pre_max = [0]*n
        suf_max = [0]*n
        pre_max[0] = height[0]
        for i in range(1,n):#最大前缀
            pre_max[i]=max(pre_max[i-1],height[i])
        suf_max[-1]=height[-1]
        for i in range(n-2,-1,-1): #最大后缀
            suf_max[i]=max(suf_max[i+1],height[i])
        
        for i in range(n-1):
            ans += min(pre_max[i],suf_max[i])-height[i]
        return ans
            

    def trap(self, height: List[int]) -> int:
        #方法二：双指针法
        #思路: 当前缀最大值小于后缀最大值时，可以直接记录这个位置的容量， 并且left左移；
        #当前缀最大值大于后缀最大值时，也可以记录相应位置的容量，然后right右移；
        #时间复杂度 o(n) 空间复杂度o(1)
        ans = 0
        n = len(height)
        left, right = 0, n-1
        pre_max, suf_max =0, 0
        while left < right:
            pre_max = max(pre_max,height[left])
            suf_max = max(suf_max,height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else :
                ans += suf_max - height[right]
                right -= 1
        
        return ans



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
