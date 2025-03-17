class Solution:
    def maximumProduct(self, nums):

        # sort the nums with ascending order        
        nums.sort()
        
        # for possible solution_#1: First three largest positive numbers
        candidate_1 = nums[-1] * nums[-2] * nums[-3]

        # for possible solution_#2: First two smallest negative numbers, whit one largest positive number.
        candidate_2 = nums[-1]*nums[0]*nums[1]
        
        max_product = max( candidate_1, candidate_2)
        
        return max_product