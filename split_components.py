from component import component

lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%&'
all_characters = lowercase_alphabet + uppercase_alphabet + digits + special_characters
special = ['.', '*', '+', '?' , '|', '[', ']', '^', '{', '}']

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
    temp_repeat_range = ''
    current_index = 0
    reversed_expression = expression[::-1]



    while current_index < len(reversed_expression):

        temp_char = reversed_expression[current_index]

        #find operator and set repeat range
        if temp_char in '*+?':
            temp_operator = temp_char
            temp_repeat_range = operator_repeat_ranges[temp_operator]
        elif temp_char == '}':
            temp_operator = 'custom'
            while True:
                current_index += 1
                temp_char = reversed_expression[current_index]
                if temp_char == '{':
                    break
                else:
                    temp_repeat_range += temp_char
            temp_repeat_range = temp_repeat_range[::-1]
            print(temp_repeat_range)
            temp_index = temp_repeat_range.find(',')
            temp_repeat_range = (int(temp_repeat_range[:temp_index]), int(temp_repeat_range[temp_index+1:]))
        else:
            temp_operator = 'string'
            temp_repeat_range = operator_repeat_ranges[temp_operator]

        #set expression for current operator
        if temp_operator in '*+?custom':
            current_index += 1
            temp_char = reversed_expression[current_index]
            temp_expression = temp_char
            current_index += 1
        else:
            if temp_char == '.':
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
        #print(temp_expression, temp_operator, temp_repeat_range)
        component_array.append(component(temp_expression, temp_operator, temp_repeat_range))
        temp_expression = ''
        temp_repeat_range = ''

    return component_array[::-1]