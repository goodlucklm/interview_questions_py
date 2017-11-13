class EditDistance(object):
    def recursive_solution(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        while i < m and i < n:
            if word1[i] != word2[i]:
                return 1+min(
                    self.recursive_solution(word1[i+1:], word2[i:]),  # remove at word1
                    self.recursive_solution(word1[i:], word2[i+1:]),  # remove at word2
                    self.recursive_solution(word1[i+1:], word2[i+1:])  # replace at word1
                )
            else:
                i += 1
        return m-i+n-i

    def dp_solution(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = []  # m+1 rows, n+1 columns
        #  declare dp array
        for i in range(m+1):
            dp.append([0]*(n+1))
        # init dp
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        # calculate the array
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1

        return dp[m][n]


    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return self.recursive_solution(word1, word2)

if __name__ == '__main__':
    ed = EditDistance()
    print ed.minDistance('horse', 'osr')