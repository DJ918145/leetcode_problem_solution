# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result < 0:
                high = mid - 1
            else:
                low = mid + 1

        return -1  # just in case
