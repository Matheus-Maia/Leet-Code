from collections import Counter
from typing import Optional, List
import re
import itertools
from csv import writer

"""
1016

Two cars (X and Y) leave in the same direction. The car X leaves with a nt d of 60 km/h and the car Y
leaves with a nt d of 90 km / h.

In one hour (60 minutes) the car Y can get a distance of 30 kilometers from the X car.

Read the distance (in km) and calculate how long it takes (in minutes) for the car Y to take this distance in
relation to the other car.

Input
The input file contains 1 integer value.

Output
Print the necessary time followed by the message "minutos" that means minutes in Portuguese.
# """


# distance = int(input())
# print(f'{distance*2} minutos')


"""
Beginner, level 1
1014

Calculate a car's average consumption being provided the total distance traveled (in Km) and the spent fuel total 
(in liters).

Input
The input file contains two values: one integer value X representing the total distance (in Km) and the second one is 
a floating point number Y  representing the spent fuel total, with a digit after the decimal point.

Output
Present a value that represents the average consumption of a car with 3 digits after the decimal point, followed by 
the message "km/l".
"""

# total_distance = int(input())
# spent_fuel = float(input())
#
# print("{:.3f}".format(total_distance/spent_fuel), "km/l")



# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#
#
# twoSum([3, 7, 11, 15], 9)

"""
Leetcode - 2169 . Count Operations to Obtain Zero

You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, 
if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.

Return the number of operations required to make either num1 = 0 or num2 = 0.
"""

# def countOperations(num1, num2):
#     count = 0
#     while num1 > 0 and num2 > 0:
#         if num1 >= num2:
#             num1 = num1 - num2
#         else:
#             num2 = num2 - num1
#         count += 1
#     return count
#
#
# print(countOperations(10, 10))


"""
Leetcode - 2170. Minimum Operations to Make the Array Alternating

You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.
"""

# step 1: find most occurence number
# step 2: find second most occurrence number >= 1 and different from number one
# step 3: go trough a list and start change the original list


# def minimumOperations(nums):
#     odd = None
#     even = None
#     operations = 0
#
#     for index, element in enumerate(nums):
#         if nums.count(element) > nums.count(odd):
#             odd = nums[index]
#
#     for index, element in enumerate(nums):
#         if nums.count(element) > nums.count(even) and nums[index] != odd:
#             even = nums[index]
#
#     for index, element in enumerate(nums):
#         if element != even and index % 2 == 0:
#             nums[index] = even
#             operations += 1
#         elif element != odd and index % 2 != 0:
#             nums[index] = odd
#             operations += 1
#
#
# minimumOperations([3,1,3,2,4,3])


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def depthFirstValues(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#
#         stack = [root]
#         values = []
#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

"""
Antes do While:
    stack == [a]
    values == []
    
Executando o while no final:

1x: 
    current = 'a'
    values = ['a']
    stack == ['c', 'b']
2x:
    current = 'b'
    values = ['a', 'b']
    stack = ['c', 'e', 'd']
3x:
    current = 'd'
    values = ['a', 'b', 'd']
    stack = ['c', 'e']
4x:
    current = 'e'
    values = ['a', 'b', 'd', 'e']
    stack = ['c']
5x:
    current = 'c'
    values = ['a', 'b', 'd', 'e', 'c']
    stack = ['f']
6x:
    current = 'f'
    values = ['a', 'b', 'd', 'e', 'c', 'f']
    stack = []
7x:
    stack == null, while é parado.
"""
#         while len(stack) > 0:
#             current = stack.pop()
#             values.append(current.val)
#
#             if current.right:
#                 stack.append(current.right)
#
#             if current.left:
#                 stack.append(current.left)
#
#         return values
#
#
# a = TreeNode('a')
# b = TreeNode('b')
# c = TreeNode('c')
# d = TreeNode('d')
# e = TreeNode('e')
# f = TreeNode('f')
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

# print(Solution().depthFirstValues(a))
#  -> ['a', 'b', 'd', 'e', 'c', 'f']


"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node.

     a
   /   \
  b     c
       / \
      d   e

Input: root = [3,9,20,null,null,15,7]
Output: 3      
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#
#         stack = [[root, 1]]
#         res = 0
#         while len(stack) > 0:
#             node, depth = stack.pop()
#
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
#         return res
#
#
# a = TreeNode('a')
# b = TreeNode('b')
# c = TreeNode('c')
# d = TreeNode('d')
# e = TreeNode('e')
#
# a.left = b
# a.right = c
# c.left = d
# c.right = e
#
#
# print(Solution().maxDepth(a))
# -> 3

"""
Leet code: 
20. Valid Parentheses 

Given a string str containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is 
valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
"""


# class Solution:
#     def isValid(self, s: str) -> bool:
#         correct_str = {'(': ')', '[': ']', '{': '}'}
#         opens = []
#
#         for symbol in s:
#             if symbol in correct_str.keys():
#                 opens.append(symbol)
#             elif opens == [] or symbol != correct_str[opens.pop()]:
#                 return False
#         return opens == []
#
#
# print(Solution().isValid("(){]"))


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two 
lists.

Return the head of the merged linked list.


"""


# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(4)
#
# a.next = b
# b.next = c
#
# x = ListNode(1)
# y = ListNode(3)
# z = ListNode(4)
#
# x.next = y
# y.next = z
#
# list1 = ListNode(a)
# list2 = ListNode(x)
#
#
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy
#
#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next
#
#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2
#         return dummy.next
#
#
# print(Solution().mergeTwoLists(a, x))


"""
LeetCode 35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             nums.append(target)
#             nums.sort()
#             return nums.index(target)
#
#
# print(Solution().searchInsert([1,3,5,6], 2))


"""
LeetCode 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest 
sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Example 2:
Input: nums = [1]
Output: 1


Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         curr_sum, max_sum = 0, nums[0]
#
#         for element in nums:
#             if curr_sum < 0:
#                 curr_sum = 0
#
#             curr_sum += element
#             max_sum = max(max_sum, curr_sum)
#
#         return max_sum
#
#
# nums = [-2, -5]
# print(Solution().maxSubArray(nums))


"""
LeetCode 70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top ?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Example 3:
input = 4
output = 5
1. 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 2 step
3. 1 step + 2 step + 1 step
4. 2 step + 1 step + 1 step
5. 2 step + 2 step

Example 4:
input n = 5
output n = 8
1. 1 step + 1 step + 1 step + 1 step + 1 step
2. 1 step + 1 step + 1 step + 2 step
3. 1 step + 1 step + 2 step + 1 step
4. 1 step + 2 step + 1 step + 1 step
5. 2 step + 1 step + 1 step + 1 step
6. 2 step + 1 step + 2 step
7. 2 step + 2 step + 1 step
8. 1 step + 2 step + 2 step
 """

# 2
# 3
# 3 + 2 = 5
# 5 + 3 = 8
# 8 + 5 = 13
# 13 + 8 = 21
# 21 + 13 = 34


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 3:
#             return n
#         else:
#             prev = 5
#             next = 3
#
#             for i in range(3, n):
#                 aux = prev + next
#                 next = prev
#                 prev = aux
#             return next
#
# print(Solution().climbStairs(3))


"""
LeetCode 94. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
b.left = c

#      1
#       \
#        2
#       /
#      3

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f


# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         stack = [root]
#         left_nodes, right_nodes = [], []
#
#         if not root:
#             return []
#
#         while len(stack) > 0:
#             current_node = stack.pop()
#
#             if current_node.right:
#                 right_nodes.append(current_node.right.val)
#                 stack.append(current_node.right)
#
#             if current_node.left:
#                 left_nodes.append(current_node.left.val)
#                 stack.append(current_node.left)
#
#         left_nodes.reverse()
#
#         if root.left:
#             left_nodes.append(root.val)
#         else:
#             left_nodes = [root.val] + left_nodes
#
#         return left_nodes + right_nodes
#
#
# print(Solution().inorderTraversal(a))


"""
LeetCode 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

# [2, 4, 1]
# [7, 2, 3, 6, 2, 8]


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy_index, sell_index, profit = 0, 0, 0
#
#         for index, element in enumerate(prices):
#             if element < prices[buy_index]:
#                 buy_index = index
#             else:
#                 sell_index = index
#                 profit = max(profit, prices[sell_index] - prices[buy_index])
#
#         return profit
#
#
# print(Solution().maxProfit([7, 2, 3, 6, 2, 8]))

"""
136. LeetCode Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""


# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return 2 * sum(set(nums)) - sum(nums)
#
# print(Solution().singleNumber([2,2,1]))


"""
283. LeetCode Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the 
non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Solução 01
        # for i in range(number_of_zeroes):
        #     nums.remove(0)
        #     nums.append(0)

        # Solução 02
        # count = 0
        #
        # while 0 in nums:
        #     nums.remove(0)
        #     count += 1
        # nums.extend([0]*count)

        # Solução 03
        # a = []
        # b = []
        # for i in nums:
        #     if i:
        #         a.append(i)
        #     else:
        #         b.append(i)
        # print(a, b)
        # nums[:] = a + b

        # Minha melhor Solução
        # nums[:] = [ele for ele in nums if ele != 0] + [0] * nums.count(0)


# Solution().moveZeroes([0, 1, 0, 3, 12])


"""
LeetCode 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element 
always exists in the array.

 

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4]
Output: 2
"""


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         return Counter(nums).most_common()[0][0]
#
# print(Solution().majorityElement([1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4]))


"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]


"""
LeetCode 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which 
is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same 
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

 
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_trad = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         res = roman_trad.get(s[0])
#
#         for i in range(1, len(s)):
#             if (s[i] == "V" or s[i] == "X") and s[i-1] == "I":
#                 res -= 2
#             elif (s[i] == "L" or s[i] == "C") and s[i-1] == "X":
#                 res -= 20
#             elif (s[i] == "D" or s[i] == "M") and s[i-1] == "C":
#                 res -= 200
#             res += roman_trad.get(s[i])
#
#         return res
#
#
# print(Solution().romanToInt("LVIII"))


"""
LeetCode 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

["a", "b", "c"]

""

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:

# Best Solution:
#         longest_common_prefix = min(strs, key=len)
#
#         for word in strs:
#             while not word.startswith(longest_common_prefix):
#                 longest_common_prefix = longest_common_prefix[:-1]
#             if len(longest_common_prefix) == 0:
#                 return ""
#
#         return longest_common_prefix


# My first Solution:
# longest_common_prefix = ""
#
# if len(strs) == 1:
#     return strs[0]
#
# if len(strs) >= 2:
#     longest_common_prefix = ""
#     first_item = strs[0]
#     second_item = strs[1]
#
#     for ele in first_item:
#         if ele in second_item:
#             longest_common_prefix += ele
#
#     if len(longest_common_prefix) == 0:
#         return ""
#
# for word in strs:
#     while not word.startswith(longest_common_prefix):
#         longest_common_prefix = longest_common_prefix[:-1]

# return longest_common_prefix

# print(Solution().longestCommonPrefix(["flower", "flow", "ight"]))


"""
LeetCode 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed 
in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the 
first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra 
memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums[:] = sorted(list(set(nums)))
#         return len(nums)


"""
LeetCode 27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order 
of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be 
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, 
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first 
k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) 
extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#
#         return len(nums)


"""
LeetCode 58. Length of Last Word

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in 
the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])
#
#
# print(Solution().lengthOfLastWord("a adkaw wjdaw kdawkd             akdwnawd       "))


"""
LeetCode 101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:


"""
Recursion studies: String Reversal

Example: 
input: the simple engineer
output: reenigne elpmis eht
"""


# class Solution():
#     def stringReversal(self, string: str) -> str:
#         if len(string) == 1:
#             return string
#
#         return string[-1] + Solution().stringReversal(string[:-1])
#
#
# print(Solution().stringReversal("the simple engineer"))


"""
Recursion studies: Palindrome

input: kayak
output: true
"""


# class Solution():
#     def isPalindrome(self, string: str) -> bool:
#         if len(string) == 1 or len(string) == 0:
#             return True
#
#         if string[0] == string[-1]:
#             return Solution().isPalindrome(string[1:-1])
#
#         return False
#
#
# print(Solution().isPalindrome("kayak"))