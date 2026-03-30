class Solution {
public:
    string largestEven(string s) {
        for(int i = s.length()-1; i>=0; i--){
            if(s[i] == '2'){
                return s;
            }
            else{
                s.pop_back();
            }
        }
        return "";
    }
};