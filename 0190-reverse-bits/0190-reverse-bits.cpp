class Solution {
public:
    string intToBinary(int n){
        string binary="";
        for(int i=31;i>=0;i--){
            binary += ((n>>i)&1) ? '1':'0';
        }
        return binary;
    }
    int reverseBits(int n) {
        string binary = intToBinary(n);
        reverse(binary.begin(), binary.end());
        cout<<"Reverserd: "<<binary;
        long dec_value = 0;
        long base = 1;
        int len = binary.length();
        for (int i = len - 1; i >= 0; i--) {
            if (binary[i] == '1')
                dec_value += base;
            base = base * 2;
        }
        return dec_value;

        
    }
};