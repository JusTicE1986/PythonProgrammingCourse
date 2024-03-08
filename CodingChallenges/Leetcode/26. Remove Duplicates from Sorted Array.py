from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums), 0, -1):
            if len(nums) <= 1:
                continue
            if nums[i - 2] == nums[i - 1]:
                nums.remove(nums[i - 1])
        k = len(nums)


