from typing import List

nums = [3,3,4]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = []
        for num in nums:
            if num not in majorityElement:
                majorityElement.append(num)
                if nums.count(num) > len(nums)/2:
                    return num
            else:
                continue




