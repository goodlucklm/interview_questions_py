import pprint

class LongestPolindromeSubString(object):
    def find_with_dp(self, s):
        n = len(s)
        if n == 0:
            return s
        lps = s[0]

        # build the table
        L = [[0 for x in range(n)] for x in range(n)]

        # all substirngs of length 1 are palindrome
        for i in range(n):
            L[i][i] = 1
        
        # loop through all possible length
        for sublen in range(2, n+1):
            for i in range(n-sublen+1):
                j = i+sublen-1
                if s[i] == s[j]:
                    if sublen == 2:
                        L[i][j] = 2
                    else:
                        if L[i+1][j-1] > 0:
                            L[i][j] = L[i+1][j-1]+2
                    if L[i][j] > len(lps):
                        lps = s[i:j+1]
        pprint.pprint(L)
        return lps

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.find_with_dp(s)

if __name__ == '__main__':
    LPS = LongestPolindromeSubString()
    s = "GEEKS FOR GEEKS"
    LPS.find_with_dp(s)
