from component import component

lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',  ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',  '}', '~']
syntax = ['[', ']', '(', ')', '{', '}', '*', '?', '+']
operators = ['*', '+', '?']
non_syntax = ['!', '"', '#', '$', '%', '&', "'", ',', '-', '/', ':', ';', '<', '=',  '>', '@', '\\', '^', '_', '`', '|', '~']
all_characters = lowercase_alphabet + uppercase_alphabet + digits + non_syntax
operator_repeat_ranges = {
        '*': (0, 10000),
        '+': (1, 10000),
        '?': (0, 1),
        'single': (1, 1)
    }

def split_components(expr):
    comp_array = []
    char_list = list(expr)
    i = 0
    while i < len(char_list):
        if char_list[i] == '\\':
            if char_list[i+1] != '\\':
                char_list[i] += char_list[i+1]
            char_list.pop(i+1)
        i+=1
    
    rev_char_list = char_list[::-1]
    index = 0

    while index < len(rev_char_list):
        operator = ''
        repeat_range = ''
        expression = ''
        character = rev_char_list[index]

        if character in operators:
            operator = character
            repeat_range = operator_repeat_ranges[operator]
            index += 1
        elif character == '}':
            operator = 'custom'

            while True:
                index += 1
                character = rev_char_list[index]
                if character == '{':
                    break
                else:
                    repeat_range += character
            repeat_range = repeat_range[::-1]
            temp_index = repeat_range.find(',')
            repeat_min = repeat_range[:temp_index]
            repeat_max = repeat_range[temp_index+1:]
            if not repeat_min:
                repeat_min = 0
            else:
                repeat_min = int(repeat_min)
            if not repeat_max:
                repeat_max = 10000
            else:
                repeat_max = int(repeat_max)
            repeat_range = (repeat_min, repeat_max)
            index += 1
        else:
            operator = 'single'
            repeat_range = operator_repeat_ranges[operator]

        character = rev_char_list[index]

        if character == ']':
            expression += character
            while character != '[':
                index += 1
                character = rev_char_list[index]
                expression += character
            expression = expression[::-1]
            index += 1
        else:
            expression = character
            index += 1

        comp_array.append(component(expression, operator, repeat_range))

    comp_array = comp_array[::-1]
    return comp_array
