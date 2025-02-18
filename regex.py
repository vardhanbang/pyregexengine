from split_components import split_components
#ignore this comment
def internal_regex(expr, input_string):
    lcomp_array = split_components(expr)
    linput_string = input_string
    while True:
        if not lcomp_array:
            if linput_string:
                return False
            else:
                return True
            
        if lcomp_array[0].verify(linput_string[:lcomp_array[0].repeat_num]):
            if (lcomp_array[0].repeat_range[1] == 10000) and (len(lcomp_array) != 1):
                temp = lcomp_array[0].repeat_num
                min_len = 0
                for i in range(temp, len(input_string)-temp):
                    if lcomp_array[1].verify(input_string[i:i+lcomp_array[1].repeat_num]):
                        continue
                    else:
                        min_len = i-1
                lcomp_array[0].repeat_range = (lcomp_array[0].repeat_range[0], min_len)
                print(f"{lcomp_array[0].expression} new range {lcomp_array[0].repeat_range}")
            while lcomp_array[0].repeat_num <= lcomp_array[0].repeat_range[1]:
                lcomp_array[0].repeat_num += 1
                if lcomp_array[0].verify(linput_string[:lcomp_array[0].repeat_num]):
                    continue
                else:
                    break
            linput_string = linput_string[lcomp_array[0].repeat_num-1:]
            lcomp_array.pop(0)
        else:
            return False
        
def regex(expression, input_string):
    text = 'α' + input_string + 'β'
    comp_array = split_components(expression)
    min_slice = 0
    for comp in comp_array:
        min_slice += comp.repeat_num
    #print(min_slice)
    slices = []
    for i in range(min_slice, len(text)+1):
        for j in range(0, len(text)-i+1):
            slices.append((j, j+i))
    matched = []
    for i,j in slices:
        if internal_regex(expression, text[i:j]):
            temp = 0
            tempi = i
            tempj = j
            if comp_array[0].expression == '^':
                tempi = 0
            else:
                tempi -= 1
            if comp_array[-1].expression == '$':
                tempj = len(text) - 2
            else:
                tempj -= 1
            matched.append((tempi,tempj))

    independent = []
    if matched:
        independent.append(matched[-1])
        for a,b in matched[::-1]:
            flag = True
            for i,j in independent:
                if (i<=a<=j) or (i<=b<=j):
                    flag = False
                    break
            if flag:
                independent.append((a,b))
    
    return independent[::-1]


#random comment ignore