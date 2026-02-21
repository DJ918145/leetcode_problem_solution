class Solution {
public:
    bool isPrime(long long n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (long long i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        }
        return true;
    }

    bool intToBinary(int n){
        int count = 0;
        while(n>0){
            if(n%2==1) count++;
            n/=2;
        }
        return isPrime(count);
    }

    int countPrimeSetBits(int left, int right) {
        int count = 0;
        for(int i = left; i<=right; i++){
            if(intToBinary(i)) count++;
        }
        return count;
    }
};