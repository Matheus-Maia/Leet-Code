from typing import Optional, List
"""
LeetCode 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""


# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#
#         return Solution().fib(n - 1) + Solution().fib(n - 2)
#
#
# print(Solution().fib(4))

"""
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php

Write a Python program to calculate the sum of a list of numbers.
"""


def calculate_sum(sum_list: List) -> int:
    if len(sum_list) == 1:
        return sum_list[0]
    return sum_list[0] + calculate_sum(sum_list[1:])


print(calculate_sum([1, 2, 3, 4, 5]))
