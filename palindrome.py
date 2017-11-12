class Palindrome(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) == 1:
            return True
        
        i = 0
        j = len(s) - 1
        while True:
            while not s[i].isalpha() and not s[i].isdigit() and i < len(s)-1:
                i += 1
            while not s[j].isalpha() and not s[j].isdigit() and j > 0:
                j -= 1
            if i >= j:
                break
            print i,j,s[i], s[j]
            if not s[i].lower() == s[j].lower():
                return False
            i += 1
            j -= 1
        return True

S = Palindrome()
print S.isPalindrome('0P')
