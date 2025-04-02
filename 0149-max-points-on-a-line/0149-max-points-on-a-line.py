class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        
        def compute_gcd(a, b):
            # Find GCD iteratively
            while b:
                a, b = b, a % b
            return a

        max_points = 0
        
        for i in range(len(points)):
            slopes = {}
            duplicates = 1  # Count the point itself
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # Check for duplicate points
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                
                # Calculate the slope as a fraction
                dx, dy = x2 - x1, y2 - y1
                divisor = compute_gcd(dx, dy)
                slope = (dx // divisor, dy // divisor)  # Represent slope as a tuple
                
                if slope not in slopes:
                    slopes[slope] = 0
                slopes[slope] += 1
            
            # Handle empty slopes dictionary
            current_max = max(slopes.values()) + duplicates if slopes else duplicates
            max_points = max(max_points, current_max)
        
        return max_points