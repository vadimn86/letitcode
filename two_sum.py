"""
Two Sum
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target. You may assume that each
input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
---
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
---
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


def two_sums(nums: List, target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if i != j:
                summ = nums[i] + nums[j]
                if summ == target:
                    return [i, j]


def main():
    nums = [2, 5, 5, 11]
    target = 10
    sums = two_sums(nums, target)

    print(f"Output: {sums}")


if __name__ == "__main__":
    main()
