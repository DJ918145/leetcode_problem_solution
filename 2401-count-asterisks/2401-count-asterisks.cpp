class Solution {
public:
    int countAsterisks(string s) {
        int count = 0;
        bool ceck = true;
        for(int i =0;i<s.size();i++){
            if(s[i]=='|'){
                ceck = !ceck;
            }
            if(ceck==true && s[i]=='*'){
                count += 1;
            }
        }
        return count;
    }
};