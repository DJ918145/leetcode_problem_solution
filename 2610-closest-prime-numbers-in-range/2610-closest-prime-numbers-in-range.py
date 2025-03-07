import math

class Solution(object):
    def sieve(self, n):
        """Precompute primes using the Sieve of Eratosthenes"""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        primes = [i for i in range(n + 1) if is_prime[i]]
        return primes, is_prime

    def closestPrimes(self, left, right):
        primes, is_prime = self.sieve(right)  # Precompute primes up to `right`

        # Filter primes in the given range [left, right]
        prime_list = [p for p in primes if left <= p <= right]

        if len(prime_list) < 2:
            return [-1, -1]  # No valid prime pairs

        # Find the closest prime pair
        min_diff = float('inf')
        ans = [-1, -1]

        for i in range(len(prime_list) - 1):
            diff = prime_list[i+1] - prime_list[i]
            if diff < min_diff:
                min_diff = diff
                ans = [prime_list[i], prime_list[i+1]]

        return ans