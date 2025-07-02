class Solution(object):
    def possibleStringCount(self, word, k):
        MOD = 10**9 + 7

        # 1) Run‐length encode word into runs r[i]
        r = []
        prev = None
        for ch in word:
            if ch == prev:
                r[-1] += 1
            else:
                r.append(1)
                prev = ch
        m = len(r)

        # Total possible without length constraint
        total = 1
        for ri in r:
            total = total * ri % MOD

        # 2) If number of runs >= k, every choice has length >= k
        if m >= k:
            return total

        # Otherwise we need to exclude those with total length < k.
        # Let y_i = x_i - 1, so sum(y_i) >= k - m = S.
        S = k - m  # > 0 here

        # dp[j] = #ways to pick y_1..y_t summing exactly to j, for j in [0..S-1]
        dp = [0] * S
        dp[0] = 1

        for ri in r:
            ci = ri - 1
            # prefix sums of dp: ps[t] = sum(dp[0..t-1])
            ps = [0] * (S + 1)
            for j in range(S):
                ps[j+1] = (ps[j] + dp[j]) % MOD

            new = [0] * S
            for j in range(S):
                # y runs from 0..ci, and we want old sum = j-y >= 0
                low = j - ci
                if low <= 0:
                    # take dp[0..j]
                    new[j] = ps[j+1]
                else:
                    # take dp[low..j]
                    new[j] = (ps[j+1] - ps[low]) % MOD
            dp = new

        bad = sum(dp) % MOD
        return (total - bad) % MOD