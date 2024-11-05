from split_components import split_components

def minimal_regex(comp_array, text):
    comp_index = 0
    slice_start = 0

    while True:
        if comp_index == len(comp_array):
            return True
        #print(slice_start)
        #print(comp_array[comp_index].repeat_range[1])
        if slice_start >= len(text) and comp_array[comp_index].repeat_num > 0:
            print(f'1 fail {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            return False
        if comp_array[comp_index].repeat_num > comp_array[comp_index].repeat_range[1]:
            print(f'2 fail {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            return False
        
        expr_length = len(comp_array[comp_index].compare_list[0])
        slice_length = expr_length*comp_array[comp_index].repeat_num

        if slice_length > len(text[slice_start:]):
            print(f'3 fail {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            return False
        if comp_array[comp_index].verify(text[slice_start:slice_start+slice_length]):
            print(f'success {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            slice_start += slice_length
            comp_index += 1
        else:
            print(f'fail {comp_array[comp_index].expression}*{comp_array[comp_index].repeat_num}')
            comp_index = max([0, comp_index - 1])
            slice_start = max([0, slice_start - comp_array[comp_index].repeat_num*len(comp_array[comp_index].compare_list[0])])
            comp_array[comp_index].repeat_num += 1

def regex(expression, input_string):
    comp_array = split_components(expression)
    minr = comp_array[-1].repeat_range[0]
    maxr = comp_array[-1].repeat_range[1]
    min_slice = 0
    for comp in comp_array:
        min_slice += comp.repeat_num*len(comp.compare_list[0])
    #print(f'min_slice: {min_slice}')
    i, j = 0, 0
    while i < len(input_string)-min_slice+1:
        print(f'slice: {input_string[i:i+min_slice]}')
        flag = False
        if minimal_regex(comp_array, input_string[i:i+min_slice]):
            flag = True
            for r in range(1, maxr - minr + 1):
                comp_array[-1].incr_r()
                if i+min_slice+r > len(input_string):
                    break
                print(f'flag slice {input_string[i:i+min_slice+r]}')
                if minimal_regex(comp_array, input_string[i:i+min_slice+r]):
                    j = i+min_slice+r
                else:
                    break
        if flag:
            break
        else:
            comp_array = split_components(expression)
            i += 1

        
    return flag, i, j