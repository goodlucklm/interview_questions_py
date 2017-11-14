class WildCardMatching(object):
    def compare_no_star(self, s, p):
        if len(s) != len(p):
            return False
        for i in range(len(s)):
            if p[i] != '?' and p[i] != s[i]:
                return False
        return True

    def find_appearances(self, key, base):
        result = []
        for i in range(len(base)-(len(key)-1)):
            matched = True
            for j in range(len(key)):
                if key[j] != '?' and key[j] != base[i+j]:
                    matched = False
                    break
            if matched:
                result.append(i)
        return result

    def isMatch_dfs(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = []
        m = len(s)
        n = len(p)
        for i in range(m+1):
            dp.append([False]*(n+1))

        dp[0][0] = True
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[m][n]

        return True

    def isMatch_recursive(self, s, p):
        while('**' in p):
            p = p.replace('**', '*')

        # match if no char and * combination
        if '*' not in p:
            return self.compare_no_star(s, p)
        else:  # compare head and tail
            n = p.find('*')
            if n > 0:
                headp = p[0:n]
                heads = s[0:n]  # no problem evenif n out of bound
                if not self.compare_no_star(heads, headp):
                    return False
                else:
                    s = s.replace(heads, '', 1)
                    p = p.replace(headp, '', 1)
            n = p.rfind('*')
            if n < len(p)-1:
                tailp = p[n+1:]
                tails = s[len(s)-len(tailp):]
                if not self.compare_no_star(tails, tailp):
                    return False
                else:
                    s = s[:len(s)-len(tails)]
                    p = p[:n+1]
        if p == '*':
            return True

        # find the first appearance of longest sub string without * in p
        lss = ''
        tmp = ''
        break_point = 0
        for i,c in enumerate(p):
            if c != '*':
                tmp += c
            else:
                if len(tmp) > len(lss):
                    lss = str(tmp)
                    break_point = i - len(lss)
                tmp = ''
        if len(tmp) > len(lss):
            lss = str(tmp)
            break_point = i - len(lss)

        # where should lss be in s
        possible_positions = self.find_appearances(lss, s)
        if len(possible_positions) == 0:
            return False

        # break into left and right, recurse
        for position in possible_positions:
            lefts = s[0: position]
            rights = s[position+len(lss):]
            leftp = p[0:break_point]
            rightp = p[break_point+len(lss):]
            if self.isMatch_recursive(lefts, leftp) and self.isMatch_recursive(rights, rightp):
                return True
        return False


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatch_dfs(s, p)
if __name__ == '__main__':
    wcm = WildCardMatching()
    print wcm.isMatch_recursive("ab", "?*")
