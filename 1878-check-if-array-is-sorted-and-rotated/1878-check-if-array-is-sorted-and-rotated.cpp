#include <vector>
#include <algorithm>

class Solution {
public:
    bool check(std::vector<int>& nums) {
        std::vector<int> sorted_nums = nums; // Copy original array
        std::sort(sorted_nums.begin(), sorted_nums.end()); // Sort the copied array
        
        int size = nums.size();
        for (int shift = 0; shift < size; shift++) { 
            // Rotate array and check for equality
            bool isEqual = true;
            for (int i = 0; i < size; i++) {
                if (nums[i] != sorted_nums[(i + shift) % size]) {
                    isEqual = false;
                    break;
                }
            }
            if (isEqual) return true; // Return true if arrays match
        }
        return false; // No rotation resulted in equality
    }
};