class Solution {
public:
    string intToBinary(int n){
        string binary = "";
        while(n>0){
            if(n%2==1) binary =  '1' + binary;
            else binary = '0' + binary;
            n /= 2;
        }
        return binary;
    }
    int binaryGap(int n) {
        string binary = intToBinary(n);
        int i = 0;
        int distance = 0;
        int len = binary.length();
        while (i < len && binary[i] != '1') i++;
        for (int j = i + 1; j < len; j++) {
            if (binary[j] == '1') {
                distance = max(distance, j - i);
                i = j; 
            }
        }
        return distance;
    }

};