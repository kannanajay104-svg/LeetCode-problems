class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def f(dp, m, n):
            if n == 0 and m == 0:
                return 1
            if m < 0 or n < 0:
                return 0
            if dp[m][n] != -1:
                return dp[m][n]
            
            dp[m][n] = f(dp, m-1, n) + f(dp, m, n-1)
            return dp[m][n]

        return f(dp, m-1, n-1)