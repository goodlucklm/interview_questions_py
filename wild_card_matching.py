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
        while('**' in p):
            p = p.replace('**', '*')

        pointer_s = 0
        pointer_p = 0
        while (pointer_s < len(s) and pointer_p < len(p)):
            # if charp is not ? or *, chars has to match charp
            if p[pointer_p] != '*' and p[pointer_p] != '?':
                if p[pointer_p] != s[pointer_s]:
                    return False
                else:  # p[pointer_p] == s[pointer_p] go to next one
                    pointer_s += 1
                    pointer_p += 1

            # if charp is ? chars matches charp
            elif p[pointer_p] == '?':
                pointer_s += 1
                pointer_p += 1

            # if charp is * find next chars match next charp
            elif p[pointer_p] == '*':
                if pointer_p == len(p)-1:
                    return True
                else:  # replace * with each possibility
                    # find the string in p after * to match with
                    char_after_star = ''
                    shift = 1
                    while (pointer_p+shift < len(p) and p[pointer_p+shift] != '*'):
                        char_after_star += p[pointer_p+shift]
                        shift += 1

                    # find appearance of char_after_star in s
                    appearences = self.find_appearances(char_after_star, s[pointer_s:])

                    # get all possible strings for *
                    possiblities = []
                    for i in appearences:
                        possiblities.append(s[pointer_s:i+pointer_s])

                    for possible in possiblities:
                        if self.isMatch(s[pointer_s:], p[pointer_p:].replace('*', possible, 1)):
                            return True
                    return False
            else:
                # should never reach here
                pass

        # p running out of char, s not
        if pointer_p == len(p) and pointer_s < len(s):
            return False
        # s running out of char, p not
        elif pointer_p < len(p) and pointer_s == len(s):
            for c in p[pointer_p:]:
                if c != '*':
                    return False
        else:
            # p and s run out of chars at the same time
            # handled by return
            pass
        return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
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
            if self.isMatch(lefts, leftp) and self.isMatch(rights, rightp):
                return True
        return False

if __name__ == '__main__':
    wcm = WildCardMatching()
    print wcm.isMatch("ab", "?*")
