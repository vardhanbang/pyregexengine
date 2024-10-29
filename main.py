from regex import regex

exp = input('enter expression: ')

while True:
    string = input('enter string: ')
    print(regex(exp, string))