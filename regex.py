lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&'
all_characters = lowercase_alphabet + uppercase_alphabet + digits
special = ['.', '*', '+', '?' , '|', '[', ']', '^']

class component:

    def __init__(self, expression, operator, repeat_range):
        self.expression = expression
        self.repeat_range = repeat_range
        self.operator = operator
        self.min_length = len(expression)

    def __str__(self):
        return f"\nexpression: {self.expression}\ncomponent type: {self.operator}\nrepeat_range: {self.repeat_range}\n"

    def verify(self, substring):
        component_matched = False
        slice_end = 0
        if self.repeat_range[0] != 0:
            slice_end += self.min_length

        for repeat_value in range(self.repeat_range[0], self.repeat_range[1] + 1):
            if len(substring) < repeat_value*self.min_length:
                return component_matched, slice_end - self.min_length

            if self.expression == '.':
                if len(substring[0:slice_end]) == repeat_value:
                    component_matched = True
                    slice_end += self.min_length
                else:
                    return component_matched, slice_end - self.min_length
            else:
                if substring[0:slice_end] == self.expression*repeat_value:
                    component_matched = True
                    slice_end += self.min_length
                else:
                    return component_matched, slice_end - self.min_length

        return component_matched, slice_end - self.min_length

def split_components(expression):

    operator_repeat_ranges = {
        '*': (0, 10000),
        '+': (1, 10000),
        '?': (0, 1),
        'string': (1, 1)
    }

    component_array = []
    temp_char = ''
    temp_expression = ''
    temp_operator = ''
    current_index = 0
    reversed_expression = expression[::-1]

    while current_index < len(reversed_expression):

        temp_char = reversed_expression[current_index]

        if temp_char in '*+?':
            temp_operator = temp_char
        else:
            temp_operator = 'string'

        if temp_operator in '*+?':
            current_index += 1
            temp_char = reversed_expression[current_index]
            temp_expression = temp_char
            current_index += 1
        else:
            while current_index < len(reversed_expression):
                temp_char = reversed_expression[current_index]
                if temp_char in all_characters:
                    temp_expression += temp_char
                    current_index += 1
                else:
                    break

        temp_expression = temp_expression[::-1]
        component_array.append(component(temp_expression, temp_operator, operator_repeat_ranges[temp_operator]))
        temp_expression = ''

    return component_array[::-1]

def regex(expression, input_string):

    component_array = split_components(expression)
    matched_substrings = []
    substring_start = 0
    substring_end = 0

    while substring_start < len(input_string):

        matched_components = []
        slice_start = 0
        slice_end = 0

        substring = input_string[substring_start:]
        substring_matched = True

        for component in component_array:
            component_matched, slice_end = component.verify(substring[slice_start:])
            if not component_matched:
                substring_matched = False
                break
            else:
                slice_end += slice_start
                matched_components.append((slice_start, slice_end))
                slice_start = slice_end
        
        if not substring_matched:
            substring_start += 1
        else:
            substring_end = matched_components[-1][1] + substring_start
            matched_substrings.append((substring_start, substring_end))
            substring_start = substring_end


    return matched_substrings


exp = input('enter expression: ')

while True:
    string = input('enter string: ')
    print(regex(exp, string))
'''

comp = component('a', 'string', (1,1))

while True:
    substr = input("enter substr: ")
    print(comp.verify(substr))

'''