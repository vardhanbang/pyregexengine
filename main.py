from regex import regex
from split_components import split_components

#exp = input('enter expression: ')

while True:
    exp = input('enter expression: ')
    comps = split_components(exp)
    for comp in comps:
        print(comp)