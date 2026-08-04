class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        key=0
        for i in nums:
            if i!=val:
                nums[key]= i
                key+=1
        return key       
            

        