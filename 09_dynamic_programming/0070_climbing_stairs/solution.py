"""
LeetCode 70. Climbing Stairs (爬楼梯)

难度: Easy
链接: https://leetcode.cn/problems/climbing-stairs/
标签: 动态规划

题目描述:
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。问有多少种不同的方法可以爬到楼顶？
"""


class Solution:
    def climbStairs_dp(self, n: int) -> int:
        """
        解法一: 动态规划

        思路:
            dp[i] = 到达第 i 阶的方法数
            dp[i] = dp[i-1] + dp[i-2]
            （从 i-1 阶走 1 步，或从 i-2 阶走 2 步）

        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs(self, n: int) -> int:
        """
        解法二: 空间优化

        思路:
            只需要前两个状态，用两个变量滚动即可。

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    assert sol.climbStairs(1) == 1, "测试用例 1 失败"
    assert sol.climbStairs(2) == 2, "测试用例 2 失败"
    assert sol.climbStairs(3) == 3, "测试用例 3 失败"
    assert sol.climbStairs(4) == 5, "测试用例 4 失败"
    assert sol.climbStairs(5) == 8, "测试用例 5 失败"
    assert sol.climbStairs(10) == 89, "测试用例 6 失败"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
