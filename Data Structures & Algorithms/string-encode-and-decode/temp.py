from typing import Any, List, Optional, Dict, Tuple
from collections import defaultdict, Counter, deque
import heapq
import math
from functools import lru_cache, cmp_to_key
import bisect
from itertools import permutations, combinations, product, accumulate
from datetime import date

# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
#
# Given an array of integers nums containing n + 1 integers where each integer
# is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this repeated number.
#
# You must solve the problem without modifying the array nums and using only
# constant extra space.
#
# Example 1:
#   Input: nums = [1,3,4,2,2]
#   Output: 2
#
# Example 2:
#   Input: nums = [3,1,3,4,2]
#   Output: 3
#
# Example 3:
#   Input: nums = [3,3,3,3,3]
#   Output: 3
#
# Constraints:
#   1 <= n <= 10^5
#   nums.length == n + 1
#   1 <= nums[i] <= n
#   All the integers in nums appear only once except for precisely one integer
#   which appears two or more times.
#
# Follow up:
#   How can we prove that at least one duplicate number must exist in nums?
#   Can you solve the problem in linear runtime complexity?




# 已解析好的表格：每行是 (姓名, 借出日期, 归还日期或 None, 是否被标红)
# 对应示例 1：today = "2016-11-30", limit = 14, 期望返回 5

def solution(blocks):
    n = len(blocks)
    i = 0
    j = i + 1
    ma = 1
    last_cnt = 0
    while j < n:
        # print(f"i: {i}, j: {j}")
        last_i = i
        while j < n and blocks[j] <= blocks[i]:
            j += 1
            i += 1
        left = i - last_i
        # print(f"left: {left}")
        last_i = i
        cnt = 0
        while j < n and blocks[j] >= blocks[i]:
            if blocks[j] == blocks[i]:
                cnt += 1
            else:
                cnt = 0
            j += 1
            i += 1
        right = i - last_i
        ma = max(ma, left + right + 1 + last_cnt)
        last_cnt = cnt
        # print(f"right: {right}")
        # print(f"ma: {ma} left + right + 1: {left + right + 1 + last_cnt} last_cnt: {last_cnt}")
    return ma


if __name__ == "__main__":
    print(solution([2, 6, 8, 5]))     # 3
    print(solution([1, 5, 5, 2, 6]))  # 4
    print(solution([1, 1]))           # 2
    print(solution([1, 2, 2]))  # 3
