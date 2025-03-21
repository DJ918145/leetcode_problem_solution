#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> romanToIntMap = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        int ans = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (i < s.size() - 1 && romanToIntMap[s[i]] < romanToIntMap[s[i + 1]]) {
                ans -= romanToIntMap[s[i]];
            } else {
                ans += romanToIntMap[s[i]];
            }
        }
        return ans;
    }
};