#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int factorial(int n) {
        if (n <= 1) return 1;
        int res = 1;
        for (int i = 2; i <= n; i++) res *= i;
        return res;
    }

    bool isDigitorialPermutation(int n) {
        int temp = n;
        long long sumOfFactorials = 0;
        string originalDigits = to_string(n);
        if (n == 0) sumOfFactorials = factorial(0);
        else {
            while (temp > 0) {
                sumOfFactorials += factorial(temp % 10);
                temp /= 10;
            }
        }
        string resultStr = to_string(sumOfFactorials);
        if (resultStr.length() != originalDigits.length()) {
            return false;
        }
        sort(originalDigits.begin(), originalDigits.end());
        sort(resultStr.begin(), resultStr.end());

        return originalDigits == resultStr;
    }
};
