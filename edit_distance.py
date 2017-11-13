class EditDistance(object):
    def shift_solution(self, word1, word2):
        m = len(word1)
        n = len(word2)
        if m < n:
            return self.shift_solution(word2, word1)

        min_distance = m
        for i in range(n+1):  # from word2[0] at word1[m/2] to word2[n-1] and word1[m/2]
            shift = m/2-i
            insert_delete_distance = abs(shift)+abs(n-(m-shift))
            replace_distance = 0
            for j in range(n):
                if j+shift >= 0 and j+shift < m:
                    if word1[j+shift] != word2[j]:
                        replace_distance += 1
            min_distance = min(min_distance, insert_delete_distance+replace_distance)
        return min_distance

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
        return self.dp_solution(word1, word2)

if __name__ == '__main__':
    ed = EditDistance()
    print ed.minDistance('abcde', 'def')