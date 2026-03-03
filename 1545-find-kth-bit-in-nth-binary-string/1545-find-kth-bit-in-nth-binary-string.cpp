class Solution {
public:
    string invert(string binary){
        string answer = "";
        for(int i = 0;i<binary.length();i++){
            if(binary[i]=='0'){
                answer += '1';
            }else{
                answer += '0';
            }
        }
        return answer;
    }
    string s(int n){
        if(n==1){
            return "0";
        }else{
            string invert_reverse = invert(s(n-1));
            reverse(invert_reverse.begin(), invert_reverse.end());
            return s(n-1) + '1' + invert_reverse;
        }
    }
    char findKthBit(int n, int k) {
        return s(n)[k-1];
    }
};