from component import component

lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&'
all_characters = lowercase_alphabet + uppercase_alphabet + digits
special = ['.', '*', '+', '?' , '|', '[', ']', '^']

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