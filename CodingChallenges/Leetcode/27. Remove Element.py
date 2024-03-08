from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    for i in range(len(nums), 0, -1):
        if nums[i - 1] == val:
            nums.remove(val)

    k = len(nums)