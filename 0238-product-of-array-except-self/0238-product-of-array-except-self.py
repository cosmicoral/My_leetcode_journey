class Solution(object):
    def productExceptSelf(self, nums):
        product = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product[i]= prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]

        return product



        
        

        return product 


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        