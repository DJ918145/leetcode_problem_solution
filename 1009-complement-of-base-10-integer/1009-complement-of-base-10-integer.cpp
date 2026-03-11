class Solution {
public:
    int bitwiseComplement(int n) {
        if(n==0) return 1;
        string binary = "";
        while(n>0){
            if(n%2==1) binary='0' + binary;
            else binary='1' + binary;
            n/=2;
        }
        cout<<binary;
        int power = 0;
        int value = 0;
        for(int i = binary.length() - 1; i >= 0; --i){
            if (binary[i] == '1') {
                value += (1 << power);
            }
            power++;
        }
        return value;
    }
};