"""
Problem: Two Sum (HashMap Approach)
-------------------------------------
Given an array of integers `nums` and an integer `target`,
return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - Only one valid answer exists
"""

def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic case
    print(two_sum([2, 7, 11, 15], 9))   # Expected: [0, 1]

    # Test 2: Numbers at end of array
    print(two_sum([3, 2, 4], 6))         # Expected: [1, 2]

    # Test 3: Same number used (different indices)
    print(two_sum([3, 3], 6))            # Expected: [0, 1]

    # Test 4: Negative numbers
    print(two_sum([-1, -2, -3, -4, -5], -8))  # Expected: [2, 4]
