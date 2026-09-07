class Solution {
    public static int f(int[][] dp,int m,int n){
        if(m==0 && n==0) return 1;
        if(n<0 || m<0) return 0;
        if(dp[m][n]!=-1) return dp[m][n];
        return dp[m][n]=f(dp,m-1,n)+f(dp,m,n-1);
    }
    public int uniquePaths(int m, int n) {
        int[][] dp=new int[m][n];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }

        return f(dp,m-1,n-1);
    }
}