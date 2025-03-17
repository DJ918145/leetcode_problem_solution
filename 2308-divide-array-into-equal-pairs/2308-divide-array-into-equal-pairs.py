class Solution(object):
    def divideArray(self, nums):
        if len(nums)%2==1:
            return False
        else:
            my_dict = {}
            for i in nums:
                if i in my_dict:
                    my_dict[i]+=1
                else:
                    my_dict[i] = 1
            for i in my_dict:
                if my_dict[i]%2==1:
                    return False
        return True
        