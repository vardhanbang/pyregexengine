from split_components import split_components

def minimal_regex(expression, text):
    comp_array = split_components(expression)
    comp_index = 0
    slice_start = 0

    while True:
        if comp_index == len(comp_array):
            return True
        if slice_start >= len(text) and len(text) > 0:
            #print('1')
            return False
        if comp_array[comp_index].repeat_num > comp_array[comp_index].repeat_range[1]:
            #print('2')
            return False
        
        expr_length = len(comp_array[comp_index].compare_list[0])
        slice_length = expr_length*comp_array[comp_index].repeat_num

        if slice_length > len(text[slice_start:]):
            #print('3')
            return False

        if comp_array[comp_index].verify(text[slice_start:slice_start+slice_length]):
            #print(f'success {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            slice_start += slice_length
            comp_index += 1
        else:
            #print(f'fail {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            comp_index = max([0, comp_index - 1])
            slice_start = max([0, slice_start - comp_array[comp_index].repeat_num*len(comp_array[comp_index].compare_list[0])])
            comp_array[comp_index].repeat_num += 1

def regex(expression, input_string):
    comp_array = split_components(expression)
    min_slice = 0
    for comp in comp_array:
        min_slice += comp.repeat_num*len(comp.compare_list[0])
    #print(f'min_slice: {min_slice}')
    for i in range(0, len(input_string)-min_slice+1):
        #print(f'slice: {input_string[i:i+min_slice]}')
        if minimal_regex(expression, input_string[i:i+min_slice]):
            return True
        
    return False