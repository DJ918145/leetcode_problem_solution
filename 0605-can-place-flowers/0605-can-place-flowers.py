class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:  # Current plot is empty
                # Check if the previous and next plots are also empty (or out of bounds)
                prev = (i == 0) or (flowerbed[i - 1] == 0)
                next = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if prev and next:
                    flowerbed[i] = 1  # Plant a flower here
                    n -= 1  # Decrease required flowers
                    if n == 0:
                        return True
        return n <= 0  # If we placed enough flowers
