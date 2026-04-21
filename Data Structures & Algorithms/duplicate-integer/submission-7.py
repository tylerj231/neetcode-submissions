class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums.sort()
        value = nums[0]
        for i in range(1, len(nums)):
            if value == nums[i]:
                return True
            value = nums[i]
        return False
