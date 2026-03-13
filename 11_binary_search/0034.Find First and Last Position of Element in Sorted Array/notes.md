# 34. Find First and Last Position of Element in Sorted Array (在排序数组中查找元素的第一个和最后一个位置)

> 难度: Medium | 分类: 二分查找 | 日期: 2026-03-09

## 题目摘要

    给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

    如果数组中不存在目标值 target，返回 [-1, -1]。

    你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

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
- [x] 选择一种区间写法并坚持使用，不要混用  今后沿用开区间的写法

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

**二分查找看似简单，但边界条件细节很多**。核心是确定并坚守"区间不变量"。今后沿用开区间（left+right）的写法，即
            循环不变量为：
            # nums[left] < target
            # nums[right] >= target
 如果函数lower_bound(nums,target)代表的是第一个x>=target的下标，那么有以下四种形式的变换：
1. 返回第一个X>=TARGET的下标：lower_bound(nums,target)
2. 返回第一个X>TARGET的下标：lower_bound(nums,target+1)
3. 返回最后一个X<=TARGET的下标：lower_bound(nums,target+1)-1
4. 返回最后一个X<TARGET的下标：lower_bound(nums,target)-1
