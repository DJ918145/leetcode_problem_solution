class Solution {
public:
    string intToBinary(int n){
        string binary = "";
        while(n>0){
            if(n%2==0) binary += "0";
            else binary += "1";
            n/=2;
        }
        return binary;
    }
    bool hasAlternatingBits(int n) {
        string binary = intToBinary(n);
        for(int i = 0; i<=binary.length()-1; i++){
            if(binary[i]==binary[i+1]) return false;
        }       
        return true;
    }
};