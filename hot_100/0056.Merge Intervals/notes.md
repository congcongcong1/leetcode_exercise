# [56]. [合并区间]

> 难度: [Medium] | 分类: [数组，排序] | 日期: 2026-3-13

## 题目摘要 

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

## 解题思路

### 第一反应
- 看到题目后最直觉的想法是什么？
 思路：进行重叠和不重叠的判断，但是数组无序，做起来比较复杂，所以要先排序


### 最终解法
- 核心思路：
  1. ...用lambda对列表中第一个元素进行排序 intervals.sort(key=lambda x: x[0])


### 复杂度分析
| 解法 | 时间复杂度 | 空间复杂度 |
|------|-----------|-----------|
| 排序 | O(nlogn) | O(1) |

## 关键知识点

- [ ] [排序]


## 踩坑记录

- ⚠️ [排序用lamda表达式更快]


## 相关题目

| 题号 | 题目 | 关系 |
|------|------|------|
| [167](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | [两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | 类似题 |
| [18](https://leetcode.cn/problems/4sum/) | [四数之和](https://leetcode.cn/problems/4sum/) | 进阶题 |

## 总结

[排序用intervals.sort(key=lambda x: x[0])]
