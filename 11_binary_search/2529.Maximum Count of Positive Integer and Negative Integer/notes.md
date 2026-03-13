# 2529. 正整数和负整数的最大计数

> 难度: Easy | 分类: 二分查找 | 日期: 2026-03-09

## 题目摘要

给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。
换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。
注意：0 既不是正整数也不是负整数。

## 解题思路

### 第一反应
- 有序数组查找 → 二分查找，O(log n)

### 最终解法
- 核心思路：每次取中间值比较，缩小搜索范围一半
- **两种区间写法**：
  - 左闭右闭 `[left, right]`：`while left <= right`，`right = mid - 1`
  - 左闭右开 `[left, right)`：`while left < right`，`right = mid`

### 复杂度分析
| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 二分查找 | O(log n) | O(1) |

## 关键知识点

- [x] 二分查找的**不变量**：搜索区间的定义决定了所有边界条件
- [x] `mid = left + (right - left) // 2` 防止整数溢出（Python 不会溢出，但这是好习惯）
- [x] 可以用官方库函数bisect_left和bisect_right来实现查找

## 踩坑记录

- ⚠️ 左闭右闭和左闭右开的 while 条件、right 更新方式不同，千万不要混淆
- ⚠️ 死循环通常是因为区间没有正确缩小

## 相关题目

| 题号 | 题目 | 关系 |
|------|------|------|
| 35 | Search Insert Position | 变体：查找插入位置 |
| 34 | Find First and Last Position | 进阶：查找边界 |
| 33 | Search in Rotated Sorted Array | 进阶：旋转数组 |

## 总结

可以用官方库函数bisect_left和bisect_right来实现查找
