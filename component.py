lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',  '}', '~']
all = lowercase_alphabet + uppercase_alphabet + digits + special
text = lowercase_alphabet + uppercase_alphabet + digits

class component:

    def __init__(self, expression, operator, repeat_range):
        self.expression = expression
        self.repeat_range = repeat_range
        self.operator = operator
        self.repeat_num = self.repeat_range[0]
        self.compare_list = []

        if self.expression[0] == '[':
            invert = False
            temp_expr = self.expression
            if self.expression[1] == '^':
                invert = True
                temp_expr = '[' + self.expression[2:]
            for i in range(1, len(temp_expr)-1):
                if '-' not in temp_expr[i-1:i+2]:
                    self.compare_list.append(temp_expr[i])
            expr = temp_expr[1:-1]
            if len(expr) < 3:
                self.compare_list += list(expr)
            else:
                for i in range(0, len(expr) - 2):
                    temp_slice = expr[i:i+3]
                    if temp_slice[1] == '-':
                        if (temp_slice[0] not in text) and (temp_slice[2] not in text):
                            self.compare_list += list(temp_slice)
                        elif temp_slice[0] in lowercase_alphabet:
                            self.compare_list += lowercase_alphabet[lowercase_alphabet.index(temp_slice[0]):lowercase_alphabet.index(temp_slice[2])+1]
                        elif temp_slice[0] in uppercase_alphabet:
                            self.compare_list += uppercase_alphabet[uppercase_alphabet.index(temp_slice[0]):uppercase_alphabet.index(temp_slice[2])+1]
                        elif temp_slice[0] in digits:
                            self.compare_list += digits[digits.index(temp_slice[0]):digits.index(temp_slice[2])+1]
            if invert:
                temp_list = self.compare_list
                self.compare_list = [i for i in all if i not in temp_list]

        elif self.expression == '.':
            self.compare_list = ['.']
            pass
        else:
            self.compare_list = [self.expression[-1]]

    def __str__(self):
        return f"expression: {self.expression}\ncomponent type: {self.operator}\nrepeat_range: {self.repeat_range}\nrepeat_num {self.repeat_num}\ncompare_list: {self.compare_list}\n"

    def verify(self, text):
        if self.expression == '^':
            return text == 'α'
        elif self.expression == '$':
            return text == 'β'
        elif self.expression == '.':
            return len(text) == self.repeat_num
        elif self.expression[0] == '[':
            if len(text) != self.repeat_num:
                return False
            else:
                for character in text:
                    if character not in self.compare_list:
                        return False
                    
            return True
        else:
            for temp_text in self.compare_list:
                if temp_text*self.repeat_num == text:
                    return True
        return False

    def incr_r(self):
        self.repeat_num += 1