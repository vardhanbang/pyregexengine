from component import component

lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',  '}', '~']
syntax = ['[', ']', '(', ')', '{', '}', '*', '?', '+']
non_syntax = ['!', '"', '#', '$', '%', '&', "'", ',', '-', '/', ':', ';', '<', '=',  '>', '@', '\\', '^', '_', '`', '|', '~']
all_characters = lowercase_alphabet + uppercase_alphabet + digits + non_syntax

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
            temp_index = temp_repeat_range.find(',')
            repeat_min = temp_repeat_range[:temp_index]
            repeat_max = temp_repeat_range[temp_index+1:]
            if not repeat_min:
                repeat_min = 0
            else:
                repeat_min = int(repeat_min)
            if not repeat_max:
                repeat_max = 10000
            else:
                repeat_max = int(repeat_max)
            temp_repeat_range = (repeat_min, repeat_max)
        else:
            temp_operator = 'string'
            temp_repeat_range = operator_repeat_ranges[temp_operator]

        #set expression for current operator
        if temp_operator in '*+?custom':
            current_index += 1
            temp_char = reversed_expression[current_index]
            temp_expression += temp_char
            if temp_char == ']':
                while temp_char != '[':
                    current_index += 1
                    temp_char = reversed_expression[current_index]
                    temp_expression += temp_char
            current_index += 1
        else:
            temp_expression += temp_char
            if temp_char == '.':
                current_index += 1
            elif temp_char == ']':
                while temp_char != '[':
                     current_index += 1
                     temp_char = reversed_expression[current_index]
                     temp_expression += temp_char
                current_index += 1
            else:
                current_index += 1
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