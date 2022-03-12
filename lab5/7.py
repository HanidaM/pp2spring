import re

def ToCamel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(ToCamel('hello_world'))
