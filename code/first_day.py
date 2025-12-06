from typing import List


def majorityElement(nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n = 0
        k = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                k = k + 1
            if k > len(nums)//2:
                n = nums[i]
            k = 1
        return n


a = majorityElement(nums=[2,2,1,1,1,2,2])

print(a)