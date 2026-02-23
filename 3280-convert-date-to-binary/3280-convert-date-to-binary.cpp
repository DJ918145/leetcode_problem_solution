class Solution {
public:
    string intToBinary(int n){
            string st = "";
            while(n>0){
                st = to_string(n%2)+st;
                n /= 2;
            }
            st += "-";
            return st;
        }
    string convertDateToBinary(string date) {
        string st = "";
        string answer = "";
        int len = date.length();
        for(int i=0;i<len+1;i++){
            if(date[i]=='-' || i==len){
                answer = answer + intToBinary(stoi(st));
                st = "";
            }
            else{
                st+=date[i];
            }
        }
        answer.pop_back();
        return answer;
    }
};