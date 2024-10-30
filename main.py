from regex import regex
from split_components import split_components
from component import component

'''
while True:
    exp = input('enter expression: ')
    comps = split_components(exp)
    for comp in comps:
        print(comp)


exp = input('enter expression: ')
for comp in split_components(exp):
        print(comp)
while True:
    inp = input("enter string: ")
    print(regex(exp, inp))



comp = component('[@#b-fC-D5-8]', 'custom', (5,19))
print(comp)
print(comp.compare_list)
'''

comp = component('.', '*', (0,10000))
print(comp.verify('bhiya@'))