class Solution {
    public int countAsterisks(String s) {
        boolean ceck = true;
        int count = 0;
        // int n = s.length();
        for(int i = 0;i<s.length();i++){
            if(s.charAt(i)=='|'){
                if(ceck==true){
                    ceck = false;
                }
                else{
                    ceck = true;
                }
            }
            if(ceck==true && s.charAt(i)=='*'){
                count = count + 1;
            }
        }
        return count;
    }
}