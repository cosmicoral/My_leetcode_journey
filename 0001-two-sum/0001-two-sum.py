class Solution(object):
    def twoSum(self, nums, target):
        seen ={}

        for i, num in enumerate(nums):
            num_to_find = target - num
            if num_to_find in seen:
                return [seen[num_to_find], i]
            seen[num] = i
        
        return []
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        