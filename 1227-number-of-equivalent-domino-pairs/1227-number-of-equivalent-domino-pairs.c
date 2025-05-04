int numEquivDominoPairs(int** dominoes, int dominoesSize, int* dominoesColSize) {
    
    int map[100]={0};
    int ans=0;
    for(int i=0;i<dominoesSize;i++)
    {
       int x=dominoes[i][0];
       int y=dominoes[i][1];
       if(x>y)
       {
         int c=x;
         x=y;
         y=c;
       }
       int key=x*10 +y;
       map[key]+=1;
       ans+=(map[key]-1);
    }
    
    return ans;
}