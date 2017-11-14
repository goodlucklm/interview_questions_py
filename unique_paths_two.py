class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = []
        for i in range(m+1):
            dp.append([0]*(n+1))

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1 and obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = 1
                elif obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m][n]

