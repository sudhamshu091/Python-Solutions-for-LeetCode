class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums[0:-1]:
            if target - i in nums[nums.index(i)+1:]:
                num = nums[nums.index(i)+1:]
                return [nums.index(i),nums.index(i)+num.index(target - i) + 1]
                break
