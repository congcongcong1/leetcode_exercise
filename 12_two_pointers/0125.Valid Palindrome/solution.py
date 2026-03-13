"""
LeetCode [125]. [验证回文串]

难度: [Easy]
链接: https://leetcode.cn/problems/valid-palindrome/
标签: [数组, 双指针,]

题目描述:
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，
短语正着读和反着读都一样。则可以认为该短语是一个回文串 。
"""

from typing import List, Optional


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        解法一:完成大写转换为小写，并移除非字母数字字符之后，用双指针方法可以轻松完成要求

        思路:完成大写转换为小写，并移除非字母数字字符之后，用双指针方法可以轻松完成要求


        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left , right  = 0, len(s) - 1
        while left <right :
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


            



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
