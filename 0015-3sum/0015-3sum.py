class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort the array first
        result = []
        size = len(nums)

        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # Skip duplicate elements for the first pointer
                continue

            # Two-pointer approach
            left, right = i + 1, size - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for the second pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result