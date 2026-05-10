class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If start is blocked
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                
                # Skip obstacle
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                
                else:
                    # Add from top
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    
                    # Add from left
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]