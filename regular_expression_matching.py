class RegularExpressionMatching(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        # init dp array
        dp = []
        for i in range(m+1):
            dp.append([False]*(n+1))

        # fill in first row, first column
        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2] or dp[0][j-1]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and i >= 2 and (s[i-1] == p[j-2] or p[j-2] == '.'))  # TODO: should really be dp[i-1][j] and p[j-1] == p[j-2]
                else:
                    dp[i][j] = False

        return dp[m][n]

if __name__ == '__main__':
    rem = RegularExpressionMatching()
    print rem.isMatch('aaa', 'ab*a')