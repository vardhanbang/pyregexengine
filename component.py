lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',  '}', '~']


class component:

    def __init__(self, expression, operator, repeat_range):
        self.expression = expression
        self.repeat_range = repeat_range
        self.operator = operator
        self.compare_list = []

        if self.expression[0] == '[':
            for i in range(1, len(self.expression)-1):
                if '-' not in self.expression[i-1:i+2]:
                    self.compare_list.append(self.expression[i])
            expr = self.expression[1:-1]
            for i in range(0, len(expr) - 2):
                temp_slice = expr[i:i+3]
                if temp_slice[1] == '-':
                    if temp_slice[0] in lowercase_alphabet:
                        self.compare_list += lowercase_alphabet[lowercase_alphabet.index(temp_slice[0]):lowercase_alphabet.index(temp_slice[2])+1]
                    if temp_slice[0] in uppercase_alphabet:
                        self.compare_list += uppercase_alphabet[uppercase_alphabet.index(temp_slice[0]):uppercase_alphabet.index(temp_slice[2])+1]
                    if temp_slice[0] in digits:
                        self.compare_list += digits[digits.index(temp_slice[0]):digits.index(temp_slice[2])+1]
        elif self.expression == '.':
            pass
        else:
            self.compare_list = [self.expression]


    def __str__(self):
        return f"\nexpression: {self.expression}\ncomponent type: {self.operator}\nrepeat_range: {self.repeat_range}\ncompare_list: {self.compare_list}\n"

    def verify(self, substring):

        component_matched = False
        slice_end = 0

        if self.expression == '.':
            if len(substring) >= self.repeat_range[0]:
                component_matched = True
                if len(substring) > self.repeat_range[1]:
                    slice_end = self.repeat_range[1]
                else:
                    slice_end = len(substring)
        else:
            for repeat_value in range(self.repeat_range[0], self.repeat_range[1] + 1):
                temp_compare_list = [compare_string*repeat_value for compare_string in self.compare_list]
                slice_end = len(temp_compare_list[0])
                if substring[:slice_end] in temp_compare_list:
                    component_matched = True
                else:
                    slice_end -= len(self.compare_list[0])
                    break
            
        return component_matched, slice_end
