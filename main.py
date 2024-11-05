from regex import regex
from split_components import split_components

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

expr = input('enter expression: ')
comps = split_components(expr)
for comp in comps:
    print(comp)


while True:
    temp = input('enter text: ')
    print(regex(expr, temp))


'''

comp = split_components('a*')[0]
print(comp)
comp.incr_r()
print(comp)

'''