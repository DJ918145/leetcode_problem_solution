class Solution {
public:
    string largestEven(std::string& s) {
        while (!s.empty() && s.back() == '1')
            s.pop_back();
        return std::move(s);
    }
};