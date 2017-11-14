class BasicCalculator(object):
    def calc_no_preth(self, s):
        operand1 = None
        operator = None
        operand2 = None
        digits = ''

        i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
            elif s[i].isdigit():
                digits += s[i]
                i += 1
            elif s[i] in ['+', '-']:
                if operand1 is None:
                    operand1 = int(digits)
                    digits = ''
                    operator = s[i]
                elif operand2 is None:
                    operand2 = int(digits)
                    digits = ''
                    if operator == '+':
                        operand1 += operand2
                    else:
                        operand1 -= operand2
                    operator = s[i]
                    operand2 = None
                else:
                    # should not reach here
                    pass
                i += 1
            else:
                # shouldn't reach here
                pass
        if len(digits) > 0 and operand1 is None:
            return int(digits)
        if len(digits) > 0 and operand2 is None:
            operand2 = int(digits)
            if operator == '+':
                operand1 += operand2
            else:
                operand1 -= operand2
        return operand1


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        while '(' in s:
            end = s.find(')')
            start = s.rfind('(', 0, end)
            s = s.replace(s[start:end+1], str(self.calc_no_preth(s[start+1:end])))
            s = s.replace('+-', '-')
            s = s.replace('-+', '-')
            s = s.replace('++', '+')
            s = s.replace('--', '+')
        if s.startswith('-') or s.startswith('+'):
            s = '0'+s
        return self.calc_no_preth(s)

if __name__ == '__main__':
    bc = BasicCalculator()
    print bc.calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))")


