class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        nums.append("zero")
        prev = nums[0]
        for i in range(len(nums) -1 ):
            if nums[i] +1 != nums[i+1]:
                if prev!=nums[i]:
                    ans.append(str(prev) + '->' + str(nums[i]))
                    prev = nums[i+1]
                else:
                    ans.append(str(nums[i]))
                    prev = nums[i+1]
        return ans
        