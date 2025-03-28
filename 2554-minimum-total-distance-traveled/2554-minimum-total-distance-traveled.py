inf = int(1e12)
class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()
        m = len(robot)
        dp = [0] + [inf] * m
        for pos, limit in factory:
            for j in range(m, 0, -1):
                cost = 0
				# for a factory, we can repair [0, min(j, factory's limit)] robots
                for k in range(1, min(limit, j) + 1):
                    cost += abs(pos - robot[j-k])
                    dp[j] = min(dp[j], dp[j-k] + cost)
        return dp[m]