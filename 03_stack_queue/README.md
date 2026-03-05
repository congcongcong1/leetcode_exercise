# 栈与队列 (Stack & Queue)

## 核心知识点
- **栈 (Stack)**：LIFO，后进先出。Python 中用 `list` 或 `collections.deque`
- **队列 (Queue)**：FIFO，先进先出。Python 中用 `collections.deque`
- **单调栈**：维护栈内元素单调性，解决"下一个更大/更小元素"类问题

## 常用解题模式
- **括号匹配**：用栈匹配左右括号
- **单调栈**：O(n) 解决 Next Greater Element 类问题
- **用栈模拟递归**：将递归改写为迭代
- **优先队列 (堆)**：`heapq` 模块

## 推荐题目

| 题号 | 题目 | 难度 | 重要度 |
|------|------|------|--------|
| 20 | Valid Parentheses | Easy | ⭐⭐⭐ |
| 155 | Min Stack | Medium | ⭐⭐⭐ |
| 232 | Implement Queue using Stacks | Easy | ⭐⭐ |
| 225 | Implement Stack using Queues | Easy | ⭐⭐ |
| 739 | Daily Temperatures | Medium | ⭐⭐⭐ |
| 496 | Next Greater Element I | Easy | ⭐⭐ |
| 84 | Largest Rectangle in Histogram | Hard | ⭐⭐⭐ |
| 150 | Evaluate Reverse Polish Notation | Medium | ⭐⭐ |
