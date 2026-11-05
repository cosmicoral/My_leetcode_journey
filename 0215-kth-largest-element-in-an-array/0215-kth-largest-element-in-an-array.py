class Solution(object):
    def findKthLargest(self, nums, k):
        rank_nums = sorted(nums, reverse=True)
        
        return rank_nums[k-1]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        