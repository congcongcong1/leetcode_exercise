"""
LeetCode 239. 滑动窗口最大值

难度: Hard
链接: https://leetcode.cn/problems/sliding-window-maximum/
标签: - hash表 数组 前缀和

题目描述:   
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #最开始想到用定长滑动窗口来解决，因为要用max(nums)来实现，总时间复杂度O(n*k),超过了时间限制
        #要在O(1)的时间内获得窗口最大值，我们需要维护一个单调队列。这个队列只记录“可能成为最大值”的元素下标。用单调队列来实现
        #用一个队列来存储下标，队首始终是当前的最大值，然后每一个元素入列时如果就把比他小的元素排除掉，因为其他元素不可能成为窗口内最大的数了，然后如果队首比left要小，即不在窗口范围内了，也把他pop掉
        # 时间复杂度 ：O(n) 每个下标最多进队入队一次，出队一次
        # 空间复杂度 ：O(n)
        ans = []*(len(nums)-k+1) #窗口个数
        q = deque() #双端队列
        for right,x in enumerate(nums):
            # 1. 元素进入队尾，同时维护队列单调性
            while q and x >= nums[q[-1]]:#当新进来的数，就把比他小的元素一个一个从队尾淘汰
                q.pop() # 排除最后一个元素
            q.append(right)

            # 2. 判断队首是不是比在窗口之外了(元素离开队首)
            left = right - k + 1
            if q[0] < left :
                q.popleft()
            
            # 3. 记录答案，只有长度为k时记录队首的值
            if left >= 0 :
                # 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans.append(nums[q[0]])
        return ans


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
