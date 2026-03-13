# 二分查找 (Binary Search)

## 核心知识点
- 前提条件：**有序**（或具有单调性的搜索空间）
- 时间复杂度 O(log n)
- 注意**边界条件**：左闭右闭 `[left, right]` vs 左闭右开 `[left, right)`

## 常用解题模式
- **标准二分**：查找目标值
- **查找边界**：第一个 ≥ target / 最后一个 ≤ target
- **二分答案**：在答案空间上二分

# 用二分查找的公式代码：
# 前提条件：有序 ，时间复杂度 O(log n)
# 用[left, right]闭区间来帮助理解   找到大于等于target的第一个下标 时间复杂度O(log n)
# 关键点：找到循环不变量： 也就是L-1不符合要求，R+1符合要求，因此移动L和R时，L = M +1 R = M -1
# while的条件：left <= right 最终推出循环时，right =left -1 因此返回的值是left 或者right+1

    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left
# 有序数组中二分查找的四种类型（下面的转换仅适用于数组中都是整数
1. 第一个大于等于x的下标： lower_bound(x)
2. 第一个大于x的下标：可以转换为`第一个大于等于 x+1 的下标` : lower_bound(x+1)
3. 最后一个小于x的下标：可以转换为`第一个大于等于 x 的下标` 的`左边位置`, lower_bound(x)-1;
4. 最后一个小于等于x的下标：可以转换为`第一个大于等于 x+1 的下标` 的 `左边位置`, lower_bound(x+1)-1;

## 推荐题目

| 题号 | 题目 | 难度 | 重要度 |
|------|------|------|--------|
| 704 | Binary Search | Easy | ⭐⭐⭐ |
| 35 | Search Insert Position | Easy | ⭐⭐ |
| 34 | Find First and Last Position of Element in Sorted Array | Medium | ⭐⭐⭐ |
| 69 | Sqrt(x) | Easy | ⭐⭐ |
| 33 | Search in Rotated Sorted Array | Medium | ⭐⭐⭐ |
| 153 | Find Minimum in Rotated Sorted Array | Medium | ⭐⭐ |
| 4 | Median of Two Sorted Arrays | Hard | ⭐⭐⭐ |
| 875 | Koko Eating Bananas | Medium | ⭐⭐⭐ |
