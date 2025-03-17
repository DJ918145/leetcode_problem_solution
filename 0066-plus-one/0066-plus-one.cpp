class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int size = digits.size();
        int count = 0;
        if(digits[size-1]==9)
        {
            for(int i =1; i<=size; i++)
            {
                if(digits[size-i]==9)
                {
                    digits[size-i]=0;
                    count = count + 1;
                }
                else
                {
                    digits[size-i]=digits[size-i]+1;
                    break;
                }
            }
        }
        else
        {
           digits[size-1]=digits[size-1]+1; 
        }
        if(count == size)
        {
            vector<int> digit;
            digit.push_back(1);
            for(int i=0; i<size;i++)
            {
                digit.push_back(0);
            }
            return digit;
        }
        else
        {
            return digits;
        }
    }
};