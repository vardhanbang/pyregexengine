from split_components import split_components
from component import component

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

    #print(matched_substrings)
    return matched_substrings
