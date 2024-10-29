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
