class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(n):
            dp[i+1] = dp[i]+dp[i-1]
        return dp[n]
