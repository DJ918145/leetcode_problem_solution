class Solution {
    public boolean isRow(int[][] mat, int i, int j){
        for(int row = 0; row<mat[0].length; row++){
            if(row == j) continue;
            else{
                if(mat[i][row]==1) return false;
            }
        }
        return true;
    }
    public boolean isCol(int[][] mat, int i, int j){
        for(int col = 0;col<mat.length; col++){
            if(col==i) continue;
            else{
                if(mat[col][j]==1) return false;
            }
        }
        return true;
    }
    public int numSpecial(int[][] mat) {
        int count = 0;
        for(int row = 0;row<mat.length; row++){
            for(int col=0;col<mat[0].length;col++){
                if(mat[row][col]==1){
                    if(isRow(mat, row, col) && isCol(mat, row, col)) count++;
                }
            }
        }
        return count;
    }
}