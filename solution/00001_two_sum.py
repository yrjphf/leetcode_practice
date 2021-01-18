# -*- coding: utf-8 -*-

from typing import List

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            num_1 = nums[i]
            for j in range(i+1, length):
                num_2 = nums[j]
                if num_1 + num_2 == target:
                    return([i, j])


class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        target_map_dict = dict()
        for i in range(length):
            num_1 = nums[i]
            target_1 = target - num_1
            target_1_index = target_map_dict.get(target_1, -1)
            if target_1_index >= 0:
                return [i, target_1_index]
            target_map_dict[num_1] = i


class Solution_3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map_dict = dict()
        for (i, num_1) in enumerate(nums):
            target_1 = target - num_1
            if target_1 in target_map_dict:
                return [i, target_map_dict[target_1]]
            target_map_dict[num_1] = i


if __name__ == '__main__':
    solution = Solution_2()
    solution.twoSum([2, 7, 11, 15], 9)
