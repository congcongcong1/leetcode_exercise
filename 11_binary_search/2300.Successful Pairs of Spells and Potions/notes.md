# 2300. 咒语和药水的成功对数

> 难度: Medium | 分类: 二分查找 | 日期: 2026-03-10

## 题目摘要

给你两个正整数数组 spells 和 potions ，按 非递减顺序 排列。只有当两个数组中元素相乘大于等于某个阈值时，咒语和药水才算成对成功。返回一个长度与 spells 相等的整数数组 answer ，其中 answer[i] 是能与第 i 个咒语配对成功的药水数目。

## 解题思路

### 第一反应
- 先排序->有序数组查找 → 二分查找，O(log n)

### 最终解法
- 核心思路：每次取中间值比较，缩小搜索范围一半
- **两种区间写法**：
  - 左闭右闭 `[left, right]`：`while left <= right`，`right = mid - 1`
  - 左闭右开 `[left, right)`：`while left < right`，`right = mid`

### 复杂度分析
| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 二分查找 | O(nlogn +mlogm) | O(1) |

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

看见无序的数组，可以用sort()排序，然后可以用官方库函数bisect_left和bisect_right来实现查找
