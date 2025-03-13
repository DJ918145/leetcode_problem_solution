class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_dict = {}
        for number in nums:
            if number in my_dict:
                my_dict[number]+=1
            else:
                my_dict[number]=1
        max_num = 0
        maxi = 0
        for key in my_dict:
            if my_dict[key]>maxi:
                maxi = my_dict[key]
                max_num = key
        return max_num
