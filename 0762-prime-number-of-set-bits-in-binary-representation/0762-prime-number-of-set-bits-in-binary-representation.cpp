class Solution {
public:
    // Since set bits for an int can't exceed 32, 
    // we can use a simple lookup or a small helper.
    bool isSmallPrime(int n) {
        return (n == 2 || n == 3 || n == 5 || n == 7 || n == 11 || 
                n == 13 || n == 17 || n == 19 || n == 23 || n == 29 || n == 31);
    }

    int countPrimeSetBits(int left, int right) {
        int totalCount = 0;
        for (int i = left; i <= right; i++) {
            // __builtin_popcount is a fast, built-in C++ function to count set bits
            int setBits = __builtin_popcount(i);
            if (isSmallPrime(setBits)) {
                totalCount++;
            }
        }
        return totalCount;
    }
};
