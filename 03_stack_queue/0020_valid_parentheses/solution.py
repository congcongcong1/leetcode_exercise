"""
LeetCode 20. Valid Parentheses (有效的括号)

难度: Easy
链接: https://leetcode.cn/problems/valid-parentheses/
标签: 栈, 字符串

题目描述:
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，
    判断字符串是否有效。
    有效条件：左括号必须用相同类型的右括号闭合，且顺序正确。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        解法: 栈

        思路:
            遇到左括号就入栈，遇到右括号就检查栈顶是否匹配。
            最终栈为空则有效。

        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        stack = []
        # 用字典存储右括号 → 左括号的映射
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # 遇到右括号：检查栈顶
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # 遇到左括号：入栈
                stack.append(char)

        # 栈为空说明所有括号都匹配了
        return len(stack) == 0


# ==================== 测试用例 ====================

def test():
    sol = Solution()

    assert sol.isValid("()") == True, "测试用例 1 失败"
    assert sol.isValid("()[]{}") == True, "测试用例 2 失败"
    assert sol.isValid("(]") == False, "测试用例 3 失败"
    assert sol.isValid("([)]") == False, "测试用例 4 失败"
    assert sol.isValid("{[]}") == True, "测试用例 5 失败"
    assert sol.isValid("") == True, "测试用例 6: 空字符串"
    assert sol.isValid("(") == False, "测试用例 7: 只有左括号"

    print("✅ 所有测试用例通过！")


if __name__ == "__main__":
    test()
