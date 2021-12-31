class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
        """
        for i,n in enumerate(nums):
            diff=target-n
            if diff in nums[i+1:]:
                return [i,nums[i+1:].index(diff)+i+1]
        """
        
